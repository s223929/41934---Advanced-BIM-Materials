## How to LCA in BIM

If you want to perform a LCA directly from your BIM model, without being slowed down by unit errors, missing materials, incomplete quantities, or broken data links, this tutorial is for you. This guide is designed to simplify the manual work, allowing you to calculate GWP quickly and efficiently using an IFC file.

---

To conduct a building LCA, one must access a various of different quantities and materials. Furthermore, the selection of all or a few impact categories must be chosen. So, there are a few things to take into account and many surprises along the way when combining LCA with BIM.

Therefore, this teaching tutorial will highlight three "_good-to-know before you start_" factors: 
1. Units, units and units
2. Extraction of materials and how it's all related
3. I have my materials - but what now?

Below, you will be presented for three code snippets, which all are a part of our _GWP comparison tool_. If you want, you can acces our tool [here](https://github.com/s223929/41934---Advanced-BIM-Materials/tree/d6ef7899e92505dc540d1205c10871eb4c35e614/A3)!

---

### 1. Units, units and units
When conducting a LCA, the units are very important, as they relate the material to the emission factor. However, it is not always easy to determine if one are extracting the IFC unit or the e.g., BlenderBIM unit. We therefore developed the code below to ensure that the correct units are consistently applied:

```
unit_assignment = ifc_file.by_type("IfcUnitAssignment")

if not unit_assignment:
    length_unit_str = "UNKNOWN"
    conversion_factor = 1.0
else:
    length_units = [
        u for u in unit_assignment[0].Units
        if u.is_a("IfcSIUnit") and u.UnitType == "LENGTHUNIT"
    ]
    if not length_units:
        length_unit_str = "UNKNOWN"
        conversion_factor = 1.0
    else:
        length_unit = length_units[0]
        prefix = length_unit.Prefix
        name = length_unit.Name
        if prefix == "MILLI":
            length_unit_str = "MILLIMETERS"
            conversion_factor = 0.001
        elif prefix == "CENTI":
            length_unit_str = "CENTIMETERS"
            conversion_factor = 0.01
        elif name == "METRE" and prefix is None:
            length_unit_str = "METERS"
            conversion_factor = 1.0
        else:
            length_unit_str = f"{prefix or ''}{name}"
            conversion_factor = 1.0

```

This code checks the IFC file to identify which length unit is used (e.g., millimeters, centimeters, or meters). The code uses the IfcUnitAssignment, where _each unit definition shall be unique; that is, there shall be no redundant unit definitions for the same unit type such as length unit or area unit_, as described by [buildingSMART](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcUnitAssignment.htm).

By applying this, the code finds the length unit, and applies the correct conversion factor so that all values are converted to meters.

---

### 2. Extraction of materials and how it's all related
The materials are one of the basis of LCA, and in BIM they can be extracted and defined in many different ways. 

A crucial attribute to know is:
> [**IfcRelAssociatesMaterial:**](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssociatesMaterial.htm) an objectified relationship between a material definition and elements or element types to which this material definition applies.

This attibute can be applied to layered elements, profiles or be arranged by identified part of a component based element: 

| Element      | Attribute |
| ----------- | ----------- |
| Layered elements   | [IfcMaterialLayerSet](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterialLayerSet.htm), [IfcMaterialLayerSetUsage](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterialLayerSetUsage.htm)        |
| Profile      | [IfcMaterialProfileSet](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterialProfileSet.htm), [IfcMaterialProfileSetUsage](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterialProfileSetUsage.htm)|
| Component based element   |  [IfcMaterialConstituentSet](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterialConstituentSet.htm)        |
| Single material   |   [IfcMaterial](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcMaterial.htm)        |

The table shows which types of material representations can be associated with an IFC element, and which IFC material type is used in each case.
In short, the "IfcMaterialLayerSet" defines what layers a component consists of - the materials and thickness. Whereas, "IfcMaterialLayerSetUsage" defines how that layer set is applied to a building element. The same is applicable for "IfcMaterialProfileSet" and "IfcMaterialProfileSetUsage". 

The following code identifies the material assigned to each exterior wall by following the IfcRelAssociatesMaterial relationship, which links a wall to its material definition. It supports both IfcMaterialLayerSetUsage and IfcMaterialLayerSet, counts the number of layers in the material set, and then categorizes each wall based on whether it has one or multiple layers.
```
walls_with_one_layer = []
walls_with_multiple_layers = []

for wall in exterior_walls:
    for rel in ifc_file.get_inverse(wall):
        if rel.is_a("IfcRelAssociatesMaterial"):
            mat = rel.RelatingMaterial

            # Support both LayerSetUsage and LayerSet
            if mat.is_a("IfcMaterialLayerSetUsage"):
                layer_set = mat.ForLayerSet
            elif mat.is_a("IfcMaterialLayerSet"):
                layer_set = mat
            else:
                continue

            num_layers = len(layer_set.MaterialLayers)
            if num_layers > 1:
                walls_with_multiple_layers.append(wall)
            elif num_layers == 1:
                walls_with_one_layer.append(wall)
            break
```

---

### 3. I have my materials - what now?

Even after extracting the materials from your BIM model, several challenges remain:

- Inconsistencies between BIM material names and the official names used in databases (e.g., Table 7 Bygningsreglementet), which makes direct matching unreliable.
- Language differences, such as materials defined in other languages (e.g. Danish) while databases use English terminology.
- Difficult to fully automate, because the workflow still requires manually selecting the correct material from Table 7 and entering it into the tool. Only then can the tool extract the corresponding values from the Excel file. In other words, the process is stil not 100% automatic.

Here is the code needed to read the Table 7 and use it within your own Python script:

```
import os
import pandas as pd
excel_filename = "Tabel-7-2025.xlsx"
excel_path = os.path.join(os.path.dirname(__file__), excel_filename)

```

This code loads the Table 7 Excel file and prepares it for use. The Excel file must be located in the same folder as your Python file.

---

### Role targeting

We target the _Analyst Level 3_ role, as the tool is developed as a standalone Python script using IfcOpenShell for a specific purpose: performing GWP calulation and comparison within a BIM workflow.

Our focus area and BIM use case in this context is _Materials_.

---

### Video

You can access our video that explains our A3 and A4 [here](https://www.youtube.com/watch?v=mbRIDSMxS1Q)!
