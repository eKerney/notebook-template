import os
import arcpy


def get_layer_from_aprx(project_path: str)-> str: 
    layer = None
    if not os.path.exists(project_path):
        print(f"Error: Project file not found at: {project_path}")
    else:
        try:
            print(f"Loading project: {project_path}")
            aprx = arcpy.mp.ArcGISProject(project_path)
            map_item = aprx.listMaps()
            for i, map in enumerate(map_item):
                print(i, map.name)
            user_input = input('enter map index:')
            index = int(user_input)
            selected_map = map_item[index]
            layer_list = selected_map.listLayers()
            for z, l in enumerate(layer_list):
                print(z, l.name)
            user_input_layer = input('enter layer index:')
            layer_ind = int(user_input_layer)
            layer = layer_list[layer_ind]
            if not layer:
                print(f"Error: Layer not found in map '{selected_map.name}'.")
                print("Available layers are: [", ", ".join(l.name for l in selected_map.listLayers()), "]")
        except Exception as e:
            print(f"An error occurred: {e}")
    return layer