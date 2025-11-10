## How to LCA in BIM

To conduct a building LCA, one must access a various of different quantities and materials. Furthermore, the selection of all or a few impact categories must be chosen. So, there is a few things to take into account.. and many surprises along the way when combining LCA with BIM.

Therefore, this teaching tutorial will highlight three "_good-to-know before you start_" factors: 
1. Units, units and units
2. Extraction of materials and how it's all related
3. I have my materials - what now?

---

### 1. Units, units and units
When conducting a LCA, the units are very important, as they relate the material to the emission factor. However, it is not always easy to determine if one are extracting the IFC unit or the e.g., BlenderBIM unit. 

**INDSÆT PY KODE TIL HVORDAN VI FINDER UNIT**

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


