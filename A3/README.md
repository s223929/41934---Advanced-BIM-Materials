## 03:

# About the tool

State the problem / claim that your tool is solving:

This tool connects BIM wall materials with EPD data (Environmental Product Declarations). It matches each material from the model with a Sorterings ID in an Excel sheet and calculates the Global Warming Potential (GWP) for each wall layer.
  
It solves the problem that this process is often done manually, which can be slow and full of mistakes. The tool makes it automatic, clear, and repeatable.

State where you found that problem:

The problem appears when doing an LCA in BIM projects. We saw that linking BIM materials to EPD data was time-consuming, so we built this tool to fix that.

Description of the tool:

Our tool is divided into several smaller Python scripts to make it easier to understand and maintain.
Each file has its own clear purpose, and together they form the full workflow for calculating the environmental impact (GWP) of wall materials in a BIM project.

- Model.py – reads and organizes data from the BIM model.
- Defining_Exterior_Walls.py – selects the exterior walls to be analysed.
- Calculate_Wall_Layer_Volumes.py – calculates the volume and thickness of each wall layer.
- Conversion_factor.py – handles unit and mass conversions.
- GWP_calculation.py – performs the Global Warming Potential (GWP) calculation.
- Tabel_7_materials_assigned.py – connects the materials from the BIM model with the EPD data in the Excel file.

Instructions to run the tool:

# Advanced Building Design

What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?

Stage C – Detailed Design / Environmental Analysis.
At this stage, we already know the main materials and can check their environmental impact using the tool.

- Which subjects might use it?

Life Cycle Assessment (LCA)

What information is required in the model for your tool to work?

- Material names
- Wall layers from a BIM model (IFC)
- Correct volumes and thickness for each layer
- EPD excel file (Table 7 - Bygningsreglementet)
  
