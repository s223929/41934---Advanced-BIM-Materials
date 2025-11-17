# About our tool

This tool links the geometric data of external walls extracted from IFC files with Environmental Product Declaration (EPD) data provided in Table 7 of BR18. It calculates the Global Warming Potential (GWP) for various user-defined wall material scenarios, enabling designers to easily compare multiple design options in terms of their environmental impact.

In other words, the tool is not only a calculation tool, but also a comparison tool that supports better and more sustainable design decisions.

----

We found calculating the GWP was non-automatic and time-consuming in the traditional software _LCAbyg_. Our tool helps solve this by making the process of comparing different scenarios easier and more organized. 

**State where you found that problem.**



----

Our tool is divided into several smaller Python scripts to make future changes or updates easier.

- Model.py – reads and organizes data from the BIM model.
- Defining_Exterior_Walls.py – selects the exterior walls to be analysed.
- Calculate_Wall_Layer_Volumes.py – calculates the volume and thickness of each wall layer.
- Conversion_factor.py – handles unit and mass conversions.
- GWP_calculation.py – performs the Global Warming Potential (GWP) calculation.
- GWP_comparison.py - calculate GWP for different materials and compare.
- Tabel_7_materials_assigned.py – connects the materials from the BIM model with the EPD data in the Excel file.

**TABLE 7 of BR18**

_Tabel-7-2025_ is integrated into the tool. Table 7 in BR18 provides standardized Global Warming Potential (GWP) values for common building materials and is used in the life cycle assessment (LCA) calculations required by BR18.
To run the tool, the user must have the corresponding Excel file open.

----
**SPØRG OM MAIN.PY**

**Instructions to run the tool**
To run the GWP comparison tool, please follow the instructions listed below:

1. Download the Python scripts (7 files in total)  and __Tabel-7-2025.xlsx__. Be sure to save all files in the same folder.
2. Run the __GWP_comparison.py__ file

The script uses input from you (the user), and what you have to input will now be described:

3. Choose your IFC file
     - The script will automatically open a folder on your folder, where you can navigate to your IFC file)
5. Choose the External wall, for which you want to calculate GWP
6. Choose the specific "Sorterings ID" related to the EPD(s) you want to map to your External wall's material layer(s)
     - Do this as many times as you have material layers and the script will calculte the GWP 
7. NOTE: the tool is only compatible for specific pre-defined units, which are suitable for wall materials, meaning that if you choose a "Sorterings ID" related to one of these non-compatible units, you will be asked to choose a new "Sorterings ID"

As you asses the GWP for your chosen materials, you will be asked if you want to compare different materials' GWP (you can do this as many times as you want): 

8. Choose between "y" (yes) or "n" (no)
9. Choose the specific "Sorterings ID" related to the EPD(s) you want to map to your External wall's material layer(s)
    - Do this as many times as you have material layers and the script will calculte the GWP
11. Choose if you want to export your results to Excel

The tool ends here - thank you for trying it out!


**Updated BPMN-diagram**
![BPMN](IMG/Group-32.svg)

# Advanced Building Design

What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?

Our tool would be useful in stage C (Detailed Design / Environmental Analysis). - CHECK IGENNEM
At this stage, we know the main materials and can check their environmental impact using this tool.

- Which subjects might use it?

This tool could be used in Life Cycle Assessment (LCA), Advanced Building Design, or in any course where students need to calculate and compare the Global Warming Potential (GWP) of materials from an IFC model.

What information is required in the model for your tool to work?

- Material names
- Wall layers from a BIM model (IFC)
- Volumes and thickness for each layer
- EPD excel file (Table 7 - Bygningsreglementet2018)

---
### 04 IDS

---
