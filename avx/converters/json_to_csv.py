import csv
import json

def convert_json_to_csv(input_file: str, output_file: str) -> None:
    """Convert json to csv.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    with open(input_file, 'r', encoding='utf-8') as jsonf:
        data = json.load(jsonf)
    if not data:
        with open(output_file, 'w', encoding='utf-8') as csvf:
            pass
        return
    if isinstance(data, list) and isinstance(data[0], dict):
        headers = list(data[0].keys())
    elif isinstance(data, dict):
        headers = list(data.keys())
        data = [data]
    else:
        raise ValueError("JSON data must be a dictionary or a list of dictionaries.")
    with open(output_file, 'w', encoding='utf-8', newline='') as csvf:
        csvWriter = csv.DictWriter(csvf, fieldnames=headers)
        csvWriter.writeheader()
        for row in data:
            csvWriter.writerow(row)
