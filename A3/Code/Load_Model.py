import ifcopenshell
from tkinter import Tk, filedialog

# The user can select an IFC file
def select_ifc_file():
    # Hide the main tkinter window
    root = Tk()
    root.withdraw()

    print("Please choose the IFC file you want to use...")
    file_path = filedialog.askopenfilename(
        title="Select IFC file",
        filetypes=[("IFC files", "*.ifc"), ("All files", "*.*")]
    )

    # Output, if the IFC file is not found
    if not file_path:
        raise FileNotFoundError("No IFC file selected. Please run again and choose a file.")

    print(f"\n IFC file selected:\n{file_path}\n")
    return file_path

# The loaded IFC file can now be loaded into another part of the code
ifc_path = select_ifc_file()
ifc_file = ifcopenshell.open(ifc_path)
