import os
import pandas as pd
from Calculate_Wall_Layer_Volumes import ifc_file, layer_volumes_summary

# ======================================================
# Load the Excel table
# ======================================================
excel_filename = "Tabel-7-2025.xlsx"
excel_path = os.path.join(os.path.dirname(__file__), excel_filename)

try:
    df = pd.read_excel(excel_path, sheet_name=0)
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find {excel_filename} in the same folder as this script.")

# Clean column names (remove spaces/newlines)
df.columns = [str(c).strip() for c in df.columns]

# Check required columns
required_cols = [
    "Sorterings ID",
    "Navn DK",
    "Global Opvarmning, modul A1-A3",
    "Global Opvarmning, modul C3",
    "Global Opvarmning, modul C4",
    "Deklareret enhed (FU)"
]

for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in Excel file. Check header names.")

# ======================================================
# User assigns Sorterings ID to each IFC material
# ======================================================
results = []

# Define the expected unit of your calculation
calculated_unit = "m³"  # Adjust if your volumes are in m² or kg

print("\nAssign a Sorterings ID to each material found in the selected wall:")
print("-------------------------------------------------------------------")

for material_name, volume in layer_volumes_summary.items():
    while True:
        user_input = input(f"Enter Sorterings ID for material '{material_name}': ").strip()
        match = df[df["Sorterings ID"].astype(str) == user_input]

        if match.empty:
            print(f"No match found for Sorterings ID '{user_input}'. Please try again.")
        else:
            # Get declared unit from Excel
            unit = match["Deklareret enhed (FU)"].values[0]

            # Check unit alignment
            if unit != calculated_unit:
                print(
                    f"Warning: Calculated unit '{calculated_unit}' does not match "
                    f"declared unit '{unit}' in Excel for '{material_name}'."
                )
            
            # Compute total GWP = A1-A3 + C3 + C4
            total_gwp = (
                match["Global Opvarmning, modul A1-A3"].fillna(0).values[0]
                + match["Global Opvarmning, modul C3"].fillna(0).values[0]
                + match["Global Opvarmning, modul C4"].fillna(0).values[0]
            )

            navn_dk = match["Navn DK"].values[0]

            results.append({
                "Material (IFC)": material_name,
                "Volume [m³]": volume,
                "Sorterings ID": user_input,
                "Navn DK": navn_dk,
                "Total GWP (A1-A3 + C3 + C4)": total_gwp,
                "Enhed": unit
            })
            break

# ======================================================
# Print Summary
# ======================================================
print("\nSummary of Assigned Materials:")
print("------------------------------------------------------------")
for r in results:
    print(
        f"- {r['Material (IFC)']} | Vol: {r['Volume [m³]']:.3f} m³ | ID: {r['Sorterings ID']} | "
        f"{r['Navn DK']} | GWP (A1-A3+C3+C4): {r['Total GWP (A1-A3 + C3 + C4)']:.3f} | Unit: {r['Enhed']}"
    )

print("------------------------------------------------------------")
print("All materials successfully assigned.")
