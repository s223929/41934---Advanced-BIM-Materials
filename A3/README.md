# About our tool

This tool links the geometric data of external walls extracted from IFC files with Environmental Product Declaration (EPD) data provided in Table 7 of BR18. It calculates the Global Warming Potential (GWP) for various user-defined wall material scenarios, enabling designers to easily compare multiple design options in terms of their environmental impact.

In other words, the tool is not only a calculation tool, but also a comparison tool that supports better and more sustainable design decisions.

----

We found calculating the GWP was non-automatic and time-consuming in the traditional software _LCAbyg_. Our tool helps solve this by making the process of comparing different scenarios easier and more organized. 

----

Our tool is divided into several smaller Python scripts to make future changes or updates easier.

- Model.py – reads and organizes data from the BIM model.
- Defining_Exterior_Walls.py – selects the exterior walls to be analysed.
- Calculate_Wall_Layer_Volumes.py – calculates the volume and thickness of each wall layer.
- Conversion_factor.py – handles unit and mass conversions.
- GWP_calculation.py – performs the Global Warming Potential (GWP) calculation.
- GWP_comparison.py - calculate GWP for different materials and compare.
- Tabel_7_materials_assigned.py – connects the materials from the BIM model with the EPD data in the Excel file.

**TABEL 7 of BR18**
_Tabel-7-2025_ is integrated into the tool. Table 7 in BR18 provides standardized Global Warming Potential (GWP) values for common building materials and is used in the life cycle assessment (LCA) calculations required by BR18.
To run the tool, the user must have the corresponding Excel file open.

----
**SPØRG OM MAIN.PY**

**Instructions to run the tool....**

![BPMN](file:///C:/Users/marie/Downloads/Group-32.svg)

# Advanced Building Design

What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?

Our tool would be useful in stage C (Detailed Design / Environmental Analysis).
At this stage, we know the main materials and can check their environmental impact using this tool.

- Which subjects might use it?

This tool could be used in Life Cycle Assessment (LCA), Advanced Building Design, or in any course where students need to calculate and compare the Global Warming Potential (GWP) of materials from an IFC model.

What information is required in the model for your tool to work?

- Material names
- Wall layers from a BIM model (IFC)
- Correct volumes and thickness for each layer
- EPD excel file (Table 7 - Bygningsreglementet)
