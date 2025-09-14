import logging
import arcgis
import arcgis.gis
import arcgis.graph
import arcgis.install
import arcgis.layers
import arcgis.map
import arcgis.notebook
from ipywidgets import Layout
from src.enums import Basemaps, ItemTypes


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


def search_content_return_item(
        gis: arcgis.GIS,
        query: str,
        max_items: int,
        item_type: ItemTypes) -> arcgis.GIS.content:
    results = gis.content.search(
        query='hydro', 
        max_items=max_items, 
        item_type=item_type.value
        )
    for i, item in enumerate(results):
        print(i, item.title)
    user_input = input('enter item index:')
    index = int(user_input)
    content = gis.content.get(results[index].id)
    return content


if __name__ == "__main__":
    main()
