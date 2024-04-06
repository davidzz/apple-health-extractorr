import os

from extractor.extractor import Extractor


class TestExtractor:
    def test_get_json(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        assert extractor.get_json() == {
            "Record": [
                {
                    "@creationDate": "2022-03-25 08:00:00 +0000",
                    "@endDate": "2022-03-25 00:00:00 +0000",
                    "@sourceName": "iPhone",
                    "@sourceVersion": "12.1",
                    "@startDate": "2022-03-25 00:00:00 +0000",
                    "@type": "HKQuantityTypeIdentifierStepCount",
                    "@unit": "count",
                    "@value": "1500"
                },
                {
                    "@creationDate": "2022-03-25 08:00:00 +0000",
                    "@endDate": "2022-03-25 12:00:00 +0000",
                    "@sourceName": "iPhone",
                    "@sourceVersion": "12.1",
                    "@startDate": "2022-03-25 12:00:00 +0000",
                    "@type": "HKQuantityTypeIdentifierStepCount",
                    "@unit": "count",
                    "@value": "2500"
                },
                {
                    "@creationDate": "2022-03-25 08:30:00 +0000",
                    "@endDate": "2022-03-25 08:30:00 +0000",
                    "@sourceName": "Apple Watch",
                    "@sourceVersion": "8.0",
                    "@startDate": "2022-03-25 08:30:00 +0000",
                    "@type": "HKQuantityTypeIdentifierHeartRate",
                    "@unit": "count/min",
                    "@value": "72"
                }
            ]}

    def test_save_to_csv(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        extractor.save_to_csv()

        assert os.path.exists("health_data.csv")
        os.remove("health_data.csv")
    def test_extract_record_types(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        assert set(extractor.get_record_types()) == {"HKQuantityTypeIdentifierStepCount",
                                                     "HKQuantityTypeIdentifierHeartRate"}

    def test_get_records_when_given_record_type(self):
        test_dir = os.path.dirname(__file__)
        health_file_path = os.path.join(test_dir, "resources", "health_data.xml")

        extractor = Extractor(file_src=health_file_path)

        assert extractor.get_records("HKQuantityTypeIdentifierStepCount") == [
            {
                "type": "HKQuantityTypeIdentifierStepCount",
                "value": "1500",
                "start_date": "2022-03-25 00:00:00 +0000",
                "end_date": "2022-03-25 00:00:00 +0000",
                "creation_date": "2022-03-25 08:00:00 +0000",
                "source_name": "iPhone",
                "unit": "count",
            }, {
                "type": "HKQuantityTypeIdentifierStepCount",
                "value": "2500",
                "start_date": "2022-03-25 12:00:00 +0000",
                "end_date": "2022-03-25 12:00:00 +0000",
                "creation_date": "2022-03-25 08:00:00 +0000",
                "source_name": "iPhone",
                "unit": "count",
            }
        ]
