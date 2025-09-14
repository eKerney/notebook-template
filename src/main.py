from enum import Enum
import logging
import arcgis
from ipywidgets import Layout
# from arcgis.gis import GIS
# from arcgis.map import Map
# from arcgis.map import Scene
# import pandas as pd


class Basemaps(Enum):
    SATELLITE = 'satellite'
    HYBRID = 'hybrid'
    TERRAIN = 'terrain'
    OCEANS = 'oceans'
    OSM = 'osm'
    DARK_GRAY_VECTOR = 'dark-gray-vector'
    GRAY_VECTOR = 'gray-vector'
    STREETS_VECTOR = 'streets-vector'
    TOPO_VECTOR = 'topo-vector'


def main():
    print("Hello from src!")


def get_GIS() -> arcgis.GIS:
    username, pwd = '', ''
    gis = arcgis.GIS()
    try:
        username = input('ArcGIS Online username:')
        pwd = input('password:')
        gis = arcgis.GIS(username=username, password=pwd)
    except Exception as e:
        logging.info(f'auth error with user {username} - generic credentials - {e}')
    return gis


def get_map(gis: arcgis.GIS, basemap: Basemaps, height: int) -> arcgis.GIS.map:
    map = gis.map()
    map.basemap.basemap = basemap.value
    map.layout = Layout(height=f'{height}px')
    return map


# def search_content_return_item():
#     results = gis.content.search(
#         query='hydro', max_items=20, item_type='Feature Service')
#     for i, item in enumerate(results):
#         print(i, item.title)
#     map_layer = gis.content.get(results[1].id)
#     map_layer


if __name__ == "__main__":
    main()
