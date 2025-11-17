## How to LCA in BIM

### Why using our tool?

If you want to perform a LCA directly from your BIM model, without being slowed down by unit errors, missing materials, incomplete quantities, or broken data links, this tutorial is for you. The tool is designed to simplify the manual work, allowing you to calculate GWP quickly and efficiently using an IFC file.

---

To conduct a building LCA, one must access a various of different quantities and materials. Furthermore, the selection of all or a few impact categories must be chosen. So, there is a few things to take into account and many surprises along the way when combining LCA with BIM.

Therefore, this teaching tutorial will highlight three "_good-to-know before you start_" factors: 
1. Units, units and units
2. Extraction of materials and how it's all related
3. I have my materials - but what now?
 
---

### 1. Units, units and units
When conducting a LCA, the units are very important, as they relate the material to the emission factor. However, it is not always easy to determine if one are extracting the IFC unit or the e.g., BlenderBIM unit. We therefore developed the code below to ensure that the correct units are consistently applied.

Python code:

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
        print("----------------------------------------------")
        print(f"Defined in the IFC model is the following unit for material layer thickess: {length_unit_str}")
        print("----------------------------------------------")

```

This code checks the IFC file to identify which length unit is used (e.g., millimeters, centimeters, or meters). It looks for the IfcUnitAssignment, finds the length unit, and sets a matching conversion factor. If no valid unit is found, it defaults to “UNKNOWN” and a factor of 1. Finally, it prints the detected unit for the material layer thickness.

---

### 2. Extraction of materials and how it's all related
The materials are one of the basis of LCA, and in BIM they can be extracted and defined in many different ways. 

A crucical attribute to know is:
> **IfcRelAssociatesMaterial:** an objectified relationship between a material definition and elements or element types to which this material definition applies.

This attibute can applied to layered elements, profiles or be arranged by identified part of a component based element: 

| Element      | Attribute |
| ----------- | ----------- |
| Layered elements   | IfcMaterialLayerSet, IfcMaterialLayerSetUsage        |
| Profile      | IfcMaterialProfileSet, IfcMaterialProfileSetUsage|
| Component based element   |  IfcMaterialConstituentSet        |
| Single material   |   IfcMaterial,  IfcMaterialList        |

**INDSÆT PY KODE TIL HVORDAN VI FINDER ET MATERIALE UNDER MATERIALLAYERSET**

---

### 3. I have my materials - what now?
- Inconsistence between defined BIM material name and e.g, Tabel 7 2025 material name
- Language difference
- Difficult to make it automatic

**EVT INDSÆT PY KODE TIL HVORDAN VI ÅBNER EXCELFIL?**


