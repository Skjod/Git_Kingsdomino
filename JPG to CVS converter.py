import os
import csv
import re

def numerical_sort(value):
    """Sorterer strenge med tal korrekt, fx tile_0_2 før tile_0_10"""
    numbers = re.findall(r'\d+', value)
    return [int(num) for num in numbers]

gt_path = r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\Predictions"
csv_file = r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\Predictions.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["board","tile_x","tile_y","tile_type","crowns"])

    # Sorter boards numerisk
    for board_folder in sorted(os.listdir(gt_path), key=numerical_sort):
        board_path = os.path.join(gt_path, board_folder)

        # Sorter filer numerisk
        for filename in sorted(os.listdir(board_path), key=numerical_sort):
            name = os.path.splitext(filename)[0]
            parts = name.split('_')

            tile_x = parts[1]
            tile_y = parts[2]
            tile_type = parts[3]
            crowns = parts[4]

            writer.writerow([board_folder, tile_x, tile_y, tile_type, crowns])

print("CSV-fil er lavet og sorteret numerisk!")