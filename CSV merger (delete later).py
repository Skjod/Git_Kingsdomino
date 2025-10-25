import os
import csv
import re

input_folder = r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\PredictionsCSV"
output_csv = "Predictions.csv"

all_rows = []

# Hjælpefunktion til at hente board nummer fra filnavn
def board_number(filename):
    match = re.search(r'board_(\d+)_predictions\.csv', filename)
    return int(match.group(1)) if match else -1

# Loop over alle CSV-filer, sorteret efter board nummer
for file in sorted(os.listdir(input_folder), key=board_number):
    if file.endswith(".csv"):
        csv_path = os.path.join(input_folder, file)
        with open(csv_path, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)  # spring header over
            for row in reader:
                all_rows.append(row)

# Skriv én samlet CSV
with open(output_csv, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["board","tile_y","tile_x","tile_type","crowns"])
    writer.writerows(all_rows)

print(f"Samlet CSV gemt: {output_csv}")