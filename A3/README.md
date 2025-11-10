# About our tool

This tool connects BIM wall materials with EPD data (Environmental Product Declarations). It calculates the Global Warming Potential (GWP) of different wall materials and allows the user/designer to compare several options and choose the material with the lowest environmental impact.

In other words, the tool is not only a calculator, it is a comparison tool that supports better design decisions.

----

We found that calculating the GWP was difficult and time-consuming, especially when comparing several materials or design options in BIM. Our tool helps solve this by making the process easier, giving a better overview of which materials are used in the exterior walls and making it easier to select and calculate the GWP for the materials.

----

Our tool is divided into several smaller Python scripts to make it easier to understand and maintain.
Each file has its own clear purpose, and together they form the full workflow for calculating the environmental impact (GWP) of wall materials in a BIM project.

- Model.py – reads and organizes data from the BIM model.
- Defining_Exterior_Walls.py – selects the exterior walls to be analysed.
- Calculate_Wall_Layer_Volumes.py – calculates the volume and thickness of each wall layer.
- Conversion_factor.py – handles unit and mass conversions.
- GWP_calculation.py – performs the Global Warming Potential (GWP) calculation.
- Tabel_7_materials_assigned.py – connects the materials from the BIM model with the EPD data in the Excel file.

----

Instructions to run the tool....

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
  
