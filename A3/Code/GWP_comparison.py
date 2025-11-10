import pandas as pd
from GWP_calculation import initial_gwp

def calculate_gwp_scenario():
    """Run a new GWP calculation for a wall configuration."""
    # Re-run Tabel_7_materials_assigned to allow user to pick new materials
    from Tabel_7_materials_assigned import results
    from Conversion_factor import converted_results

    gwp_per_material = {}
    total_gwp = 0

    for r in results:
        material_name_ifc = r["Material (IFC)"]
        epd_name = r["Navn DK"]
        total_gwp_per_unit = r["Total GWP (A1-A3 + C3 + C4)"]
        converted_unit = converted_results.get(material_name_ifc)

        if converted_unit is None:
            gwp = None
        else:
            gwp = total_gwp_per_unit * converted_unit
            total_gwp += gwp

        gwp_per_material[material_name_ifc] = {
            "EPD name": epd_name,
            "GWP_total": gwp,
            "Unit": r["Enhed"]
        }

    return gwp_per_material, total_gwp


def main():
    print("=== GWP Comparison Tool ===")

    # Store all scenarios here
    scenarios = []
    scenario_counter = 1

    # Add original (imported from GWP_calculation.py)
    total_original = sum(v["GWP_total"] for v in initial_gwp.values() if v["GWP_total"] is not None)
    scenarios.append({
        "Scenario": f"Original ({scenario_counter})",
        "Total GWP (kg CO2-eq)": total_original
    })

    # Iterative loop
    while True:
        answer = input("\nDo you want to calculate an alternative scenario? (y/n): ").strip().lower()
        if answer != "y":
            break

        scenario_counter += 1
        gwp_dict, total_gwp = calculate_gwp_scenario()
        scenarios.append({
            "Scenario": f"Alternative {scenario_counter - 1}",
            "Total GWP (kg CO2-eq)": total_gwp
        })

    # Display results in table form
    df = pd.DataFrame(scenarios)
    df["Difference from Original (%)"] = (
        (df["Total GWP (kg CO2-eq)"] - df.loc[0, "Total GWP (kg CO2-eq)"])
        / df.loc[0, "Total GWP (kg CO2-eq)"] * 100
    ).round(2)

    print("\n=== GWP Comparison Summary ===")
    print(df.to_string(index=False))

    # Optionally save to Excel
    save = input("\nDo you want to save the results to Excel? (y/n): ").strip().lower()
    if save == "y":
        df.to_excel("GWP_comparison_results.xlsx", index=False)
        print("✅ Results saved to 'GWP_comparison_results.xlsx'.")

if __name__ == "__main__":
    main()
