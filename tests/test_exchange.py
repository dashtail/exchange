# test_exchange_processor.py
import unittest
from src.exchange_processor import process_operations


class TestExchangeProcessor(unittest.TestCase):
    def test_case_1(self):
        input_data = {
            "balance": 10000.0,
            "limit": 10000.0,
            "operations": [
                {
                    "type": "In",
                    "spot": 1.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-19T21:07:22.556467",
                },
                {
                    "type": "Out",
                    "spot": 1.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-20T21:07:22.556467",
                },
            ],
        }

        expected_output = {
            "client_info": {"balance": 10000.0, "limit": 0.0},
            "operations": [
                {"real_quantity": 5000.0, "created_at": "2023-07-19T21:07:22.556467"},
                {"real_quantity": -5000.0, "created_at": "2023-07-20T21:07:22.556467"},
            ],
        }

        actual_output = process_operations(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_case_2(self):
        input_data = {
            "balance": 10000.0,
            "limit": 10000.0,
            "operations": [
                {
                    "type": "In",
                    "spot": 1.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-19T21:07:22.556467",
                },
                {
                    "type": "Out",
                    "spot": 1.0,
                    "spread": 0.0,
                    "fx_quantity": 6000.0,
                    "created_at": "2023-07-20T21:07:22.556467",
                },
                {
                    "type": "In",
                    "spot": 1.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-20T21:07:22.559999",
                },
            ],
        }

        expected_output = {
            "client_info": {"balance": 20000.0, "limit": 0.0},
            "operations": [
                {"real_quantity": 5000.0, "created_at": "2023-07-19T21:07:22.556467"},
                {"real_quantity": 5000.0, "created_at": "2023-07-20T21:07:22.559999"},
            ],
        }

        actual_output = process_operations(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_case_3(self):
        input_data = {
            "balance": 10000.0,
            "limit": 10000.0,
            "operations": [
                {
                    "type": "In",
                    "spot": 2.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-19T21:07:22.556467",
                },
                {
                    "type": "Out",
                    "spot": 2.0,
                    "spread": 0.0,
                    "fx_quantity": 6000.0,
                    "created_at": "2023-07-20T21:07:22.556467",
                },
                {
                    "type": "In",
                    "spot": 2.0,
                    "spread": 0.0,
                    "fx_quantity": 5000.0,
                    "created_at": "2023-07-20T21:07:22.559999",
                },
            ],
        }

        expected_output = {
            "client_info": {"balance": 20000.0, "limit": 0.0},
            "operations": [
                {"real_quantity": 10000.0, "created_at": "2023-07-19T21:07:22.556467"}
            ],
        }

        actual_output = process_operations(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_case_4(self):
        input_data = {
            "balance": 5000.0,
            "limit": 20000.0,
            "operations": [
                {
                    "type": "In",
                    "spot": 1.0,
                    "spread": 0.5,
                    "fx_quantity": 10000.0,
                    "created_at": "2023-07-19T21:07:22.556467",
                },
                {
                    "type": "Out",
                    "spot": 1.0,
                    "spread": 0.5,
                    "fx_quantity": 10000.0,
                    "created_at": "2023-07-20T21:07:22.556467",
                },
            ],
        }

        expected_output = {
            "client_info": {"balance": -5000.0, "limit": 0.0},
            "operations": [
                {"real_quantity": 5000.0, "created_at": "2023-07-19T21:07:22.556467"},
                {"real_quantity": -15000.0, "created_at": "2023-07-20T21:07:22.556467"},
            ],
        }

        actual_output = process_operations(input_data)
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
