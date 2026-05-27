import csv
import json

def convert_csv_to_json(input_file: str, output_file: str) -> None:
    """Convert csv to json.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    data = []
    with open(input_file, 'r', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)
    with open(output_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
