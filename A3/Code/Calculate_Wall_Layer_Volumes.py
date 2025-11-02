from collections import defaultdict
from Defining_Exterior_Walls import ifc_file, selected_wall_type

# loading user selected wall

# Identify the selected wall
def get_wall_identifier(wall):
    if wall.ObjectType:
        return wall.ObjectType
    elif wall.Name:
        return wall.Name
    else:
        return f"Unnamed wall #{wall.id()}"


# Finding all walls corresponding to the selected type
selected_walls = [
    wall
    for wall in (ifc_file.by_type("IfcWall") + ifc_file.by_type("IfcWallStandardCase"))
    if get_wall_identifier(wall) == selected_wall_type
]

if not selected_walls:
    raise ValueError(f"No wall found for the selected type: {selected_wall_type}")


# Getting the wall area from defined property sets
def get_wall_area(wall):
    """Finds area under Object Information → Instance → Dimensions"""
    for rel in getattr(wall, "IsDefinedBy", []):
        if rel.is_a("IfcRelDefinesByProperties"):
            prop_def = rel.RelatingPropertyDefinition
            if prop_def.is_a("IfcPropertySet"):
                for prop in prop_def.HasProperties:
                    if prop.Name.lower() in ["area", "grosssidearea", "netsidearea"]:
                        nominal_value = getattr(prop, "NominalValue", None)
                        if nominal_value:
                            return float(nominal_value.wrappedValue)
    # Output, if no wall area found in property sets
    print(
        f"There is no information on area for object {get_wall_identifier(wall)}. "
        "Please adjust BIM-model to include area under Object Information → Dimensions."
    )
    return None


# Getting the different layers' thickness from different ways of defining thicknesses
def get_layer_thickness(layer):
    if hasattr(layer, "LayerThickness") and layer.LayerThickness:
        return layer.LayerThickness

    material = getattr(layer, "Material", None)
    if not material:
        return None

    # IfcMaterialLayerSetUsage / LayerSet
    if hasattr(material, "ForLayerSet"):
        layer_set = material.ForLayerSet
        if hasattr(layer_set, "MaterialLayers"):
            for l in layer_set.MaterialLayers:
                if hasattr(l, "LayerThickness") and l.LayerThickness:
                    return l.LayerThickness

    # IfcMaterialList
    if hasattr(material, "MaterialList"):
        for mat in material.MaterialList:
            if hasattr(mat, "LayerThickness") and mat.LayerThickness:
                return mat.LayerThickness

    # IfcMaterialConstituentSet
    if hasattr(material, "HasConstituents"):
        for c in material.HasConstituents:
            if hasattr(c, "LayerThickness") and c.LayerThickness:
                return c.LayerThickness

    return None


# Calculating the volumens of the different wall materials
def calculate_layer_volumes(wall):
    volumes = []
    area = get_wall_area(wall)
    if area is None:
        return volumes

    # Find material layers
    for rel in ifc_file.get_inverse(wall):
        if rel.is_a("IfcRelAssociatesMaterial"):
            mat = rel.RelatingMaterial

            if mat.is_a("IfcMaterialLayerSetUsage"):
                layer_set = mat.ForLayerSet
            elif mat.is_a("IfcMaterialLayerSet"):
                layer_set = mat
            else:
                continue

            # Calculate volumes per layer
            for layer in layer_set.MaterialLayers:
                thickness = get_layer_thickness(layer)
                material_name = getattr(layer.Material, "Name", "Unnamed Material")

                # Output, if no thickness is defined for the material
                if thickness is None:
                    print(
                        f"There is no information on thickness for layer '{material_name}' "
                        f"in object {get_wall_identifier(wall)}. "
                        "Please adjust BIM-model to include thickness."
                    )
                    continue

                volume = thickness * area
                volumes.append((material_name, volume))
            break

    return volumes


# Aggregate total volume per material across all walls
layer_volumes_summary = defaultdict(float)

for wall in selected_walls:
    wall_volumes = calculate_layer_volumes(wall)
    for material_name, volume in wall_volumes:
        layer_volumes_summary[material_name] += volume


# Printing summary output
print(f"\nThis wall type has {len(selected_walls)} different wall objects.")
print("\nTotal volumes per material:")
for material, total_volume in layer_volumes_summary.items():
    print(f"- {material}: {total_volume:.3f} m³")

# Now the variable can be used in other parts of the code - for calculating GWP
layer_volumes_summary = dict(layer_volumes_summary)

