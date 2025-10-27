import ifcopenshell
from tkinter import Tk, filedialog

# === Function to let the user select an IFC file ===
def select_ifc_file():
    # Hide the main tkinter window
    root = Tk()
    root.withdraw()

    print("Please choose the IFC file you want to use...")
    file_path = filedialog.askopenfilename(
        title="Select IFC file",
        filetypes=[("IFC files", "*.ifc"), ("All files", "*.*")]
    )

    if not file_path:
        raise FileNotFoundError("No IFC file selected. Please run again and choose a file.")

    print(f"\n IFC file selected:\n{file_path}\n")
    return file_path

# === Load and store the IFC file as a reusable variable ===
ifc_path = select_ifc_file()
ifc_file = ifcopenshell.open(ifc_path)
