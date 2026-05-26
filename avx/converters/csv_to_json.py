import csv, json

def convert_csv_to_json(input_file: str, output_file: str) -> None:
    """Convert csv to json."""
    data = []
    with open(input_file, 'r', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)
    with open(output_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
