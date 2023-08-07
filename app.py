import json
from src.exchange_processor import process_operations


def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def write_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    input_data = read_json("./data/input.json")
    output_data = process_operations(input_data)
    write_json(output_data, "./data/output.json")
