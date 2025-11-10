## How to LCA in BIM

To conduct a building LCA, one must access a various of different quantities and materials. Furthermore, the selection of all or a few impact categories must be chosen. So, there is a few things to take into account.. and many surprises along the way when combining LCA with BIM.

Therefore, this teaching tutorial will highlight three "_good-to-know before you start_" factors: 
- Units, units and units
- Extraction of materials and how it's all related
- I have my material names - what now?

---

### Units, units and units
When conducting a LCA, the units are very important, as they relate the material to the emission factor. However, it is not always easy to determine if one are extracting the IFC unit or the e.g., BlenderBIM unit. 

ifc_file.by_type("IfcUnitAssignment")

IfcSIUnit...
... 


---

### Extraction of materials and how it's all related
The materials are one of the basis of LCA, and in BIM they can be extracted and defined in many different ways. 

A crucical attribute to know is:
> **IfcRelAssociatesMaterial:** an objectified relationship between a material definition and elements or element types to which this material definition applies.

These materials can applied to layered elements, profiles or be arranged by identified part of a component based element: 

| Element      | Attribute |
| ----------- | ----------- |
| Layered elements   | IfcMaterialLayerSet, IfcMaterialLayerSetUsage        |
| Profile      | IfcMaterialProfileSet, IfcMaterialProfileSetUsage|
| Component based element   |  IfcMaterialConstituentSet        |
| Single material   |   IfcMaterial,  IfcMaterialList        |

---

### I have my material names - what now?
