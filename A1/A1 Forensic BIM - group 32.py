import ifcopenshell
import ifcopenshell.util.element

#REMEMBER TO MODIFY THE MODEL PATH
model = ifcopenshell.open(r"C:\Users\oline\OneDrive - Danmarks Tekniske Universitet\1. semester\25-16-D-ARCH.ifc") 

#Defines the different roofs
Roof_types = set()
for rt in model.by_type("IfcRoof"):
    if rt.Name:
        Roof_types.add(rt.Name)

print("Number of different roof types:", len(Roof_types))
print("\nList of roof types used in the model:")
for r in sorted(Roof_types):
    print("-", r)


#Defines a dictionary for roof materials
Roof_materials = set()

#The materials can be found in different places in Ifc - therefore the "if" is used three times 
for roof in model.by_type("IfcRoof"):
    for rel in roof.HasAssociations:
        mat = rel.RelatingMaterial
        if mat.is_a("IfcMaterial"):
            if mat.Name:
                Roof_materials.add(mat.Name)
        elif mat.is_a("IfcMaterialLayerSet"):
            for layer in mat.MaterialLayers:
                if layer.Material and layer.Material.Name:
                    Roof_materials.add(layer.Material.Name)
        elif mat.is_a("IfcMaterialList"):
            for m in mat.Materials:
                if m.Name:
                    Roof_materials.add(m.Name)


print("\nNumber of different roof materials:", len(Roof_materials))

#The materials are listed alphabetical
print("\nList of unique roof materials used in the model:")
for m in sorted(Roof_materials):
    print("-", m)





