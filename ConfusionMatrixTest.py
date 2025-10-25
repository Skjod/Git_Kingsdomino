import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

# Læs GroundTruth og Predictions
gt = pd.read_csv(r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\GroundTruth.csv")
pred = pd.read_csv(r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\Predictions.csv")

# Sørg for at begge dataframes er sorteret på board, tile_y, tile_x
gt = gt.sort_values(['board', 'tile_y', 'tile_x']).reset_index(drop=True)
pred = pred.sort_values(['board', 'tile_y', 'tile_x']).reset_index(drop=True)

# --- Tile type confusion matrix ---
y_true_tile = gt['tile_type']
y_pred_tile = pred['tile_type']

types = sorted(gt['tile_type'].unique())  # alle unikke labels
cm_tile = confusion_matrix(y_true_tile, y_pred_tile, labels=types)

print("Tile Type Confusion Matrix:")
print(pd.DataFrame(cm_tile, index=types, columns=types))
print("\nClassification Report:")
print(classification_report(y_true_tile, y_pred_tile, labels=types, zero_division=0))

# --- Crowns confusion matrix ---
y_true_crowns = gt['crowns']
y_pred_crowns = pred['crowns']

crowns_labels = sorted(gt['crowns'].unique())
cm_crowns = confusion_matrix(y_true_crowns, y_pred_crowns, labels=crowns_labels)

print("Crowns Confusion Matrix:")
print(pd.DataFrame(cm_crowns, index=crowns_labels, columns=crowns_labels))
print("\nClassification Report:")
print(classification_report(y_true_crowns, y_pred_crowns, labels=crowns_labels, zero_division=0))