import csv
import json
from pathlib import Path

data_dir = Path(__file__).parent/"data"
output_dir = Path(__file__).parent/"output"

def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump(rows, f, indent=4)

        print(f"Successfully converted  {csv_file} -> {json_file}")
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    csv_file = data_dir/"user.csv"
    json_file = output_dir/"user.json"
    csv_to_json(csv_file, json_file)