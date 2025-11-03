from collections import defaultdict
from Defining_Exterior_Walls import ifc_file, selected_wall_type

# ======================================================
# IFC Unit Assignment Checker
# ======================================================
unit_assignment = ifc_file.by_type("IfcUnitAssignment")

if not unit_assignment:
    print("No unit assignment found in the IFC file.")
    length_unit_str = "UNKNOWN"
else:
    # There can be multiple units; find the length unit
    length_units = [
        u for u in unit_assignment[0].Units
        if u.is_a("IfcSIUnit") and u.UnitType == "LENGTHUNIT"
    ]

    if not length_units:
        print("No length unit found in the IFC file.")
        length_unit_str = "UNKNOWN"
    else:
        length_unit = length_units[0]
        prefix = length_unit.Prefix  # e.g., MILLI, CENTI, or None
        name = length_unit.Name      # e.g., METRE

        # Reconstruct readable unit
        if prefix == "MILLI":
            length_unit_str = "MILLIMETERS"
        elif prefix == "CENTI":
            length_unit_str = "CENTIMETERS"
        elif name == "METRE" and prefix is None:
            length_unit_str = "METERS"
        else:
            length_unit_str = f"{prefix or ''}{name}"

        print(f"Defined in the IFC model is the follwing unit: {length_unit_str} ")

# ======================================================
# Identify the selected wall
# ======================================================
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


# ======================================================
# Getting the wall area
# ======================================================
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
    print(
        f"There is no information on area for object {get_wall_identifier(wall)}. "
        "Please adjust BIM-model to include area under Object Information → Dimensions."
    )
    return None


# ======================================================
# Getting layer thickness
# ======================================================
def get_layer_thickness(layer):
    if hasattr(layer, "LayerThickness") and layer.LayerThickness:
        return layer.LayerThickness

    material = getattr(layer, "Material", None)
    if not material:
        return None

    if hasattr(material, "ForLayerSet"):
        layer_set = material.ForLayerSet
        if hasattr(layer_set, "MaterialLayers"):
            for l in layer_set.MaterialLayers:
                if hasattr(l, "LayerThickness") and l.LayerThickness:
                    return l.LayerThickness

    if hasattr(material, "MaterialList"):
        for mat in material.MaterialList:
            if hasattr(mat, "LayerThickness") and mat.LayerThickness:
                return mat.LayerThickness

    if hasattr(material, "HasConstituents"):
        for c in material.HasConstituents:
            if hasattr(c, "LayerThickness") and c.LayerThickness:
                return c.LayerThickness

    return None


# ======================================================
# Calculating layer volumes
# ======================================================
def calculate_layer_volumes(wall):
    volumes = []
    area = get_wall_area(wall)
    if area is None:
        return volumes

    for rel in ifc_file.get_inverse(wall):
        if rel.is_a("IfcRelAssociatesMaterial"):
            mat = rel.RelatingMaterial

            if mat.is_a("IfcMaterialLayerSetUsage"):
                layer_set = mat.ForLayerSet
            elif mat.is_a("IfcMaterialLayerSet"):
                layer_set = mat
            else:
                continue

            for layer in layer_set.MaterialLayers:
                thickness = get_layer_thickness(layer)
                material_name = getattr(layer.Material, "Name", "Unnamed Material")

                if thickness is None:
                    print(
                        f"There is no information on thickness for layer '{material_name}' "
                        f"in object {get_wall_identifier(wall)}. "
                        "Please adjust BIM-model to include thickness."
                    )
                    continue

                # Assume values are already in meters (IFC standard practice)
                volume = thickness * area
                volumes.append((material_name, volume))
            break

    return volumes


# ======================================================
# Summarize total volumes per material
# ======================================================
layer_volumes_summary = defaultdict(float)

for wall in selected_walls:
    wall_volumes = calculate_layer_volumes(wall)
    for material_name, volume in wall_volumes:
        layer_volumes_summary[material_name] += volume

# ======================================================
# Output
# ======================================================
print(f"\n{len(selected_walls)} exterior walls have been identified to match the selected wall type.")
print("\nTotal volumes per material:")
for material, total_volume in layer_volumes_summary.items():
    print(f"- {material}: {total_volume:.3f} m³")

# Now the variable can be used in other parts of the code - for calculating GWP
layer_volumes_summary = dict(layer_volumes_summary)
