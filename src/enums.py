from enum import Enum


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


class ItemTypes(Enum):
    WEB_MAP = "Web Map"
    FEATURE_SERVICE = "Feature Service"
    MAP_SERVICE = "Map Service"
    IMAGE_SERVICE = "Image Service"
    SCENE_SERVICE = "Scene Service"
    VECTOR_TILE_SERVICE = "Vector Tile Service"
    WMS = "WMS"
    WMTS = "WMTS"
    KML = "KML"
    SHAPEFILE = "Shapefile"
    CSV = "CSV"
    LAYER_PACKAGE = "Layer Package"
    MOBILE_MAP_PACKAGE = "Mobile Map Package"
    PROJECT_PACKAGE = "Project Package"
    TILE_PACKAGE = "Tile Package"
    VECTOR_TILE_PACKAGE = "Vector Tile Package"
    LOCATOR_PACKAGE = "Locator Package"
    GEOPROCESSING_PACKAGE = "Geoprocessing Package"
    DEEP_LEARNING_PACKAGE = "Deep Learning Package"
    DESKTOP_APPLICATION_TEMPLATE = "Desktop Application Template"
    WEB_MAPPING_APPLICATION = "Web Mapping Application"
    FEATURE_COLLECTION = "Feature Collection"
    FEATURE_COLLECTION_TEMPLATE = "Feature Collection Template"
    WEB_SCENE = "Web Scene"
    DASHBOARD = "Dashboard"
    STORYMAP = "StoryMap"
    HUB_SITE_APPLICATION = "Hub Site Application"
    HUB_PAGE = "Hub Page"
    NOTEBOOK = "Notebook"
    KNOWLEDGE_BASE = "Knowledge Base"
    DOCUMENT_LINK = "Document Link"
    CAD_DRAWING = "CAD Drawing"
    BIG_DATA_FILE_SHARE = "Big Data File Share"
    BIG_DATA_ANALYTIC = "Big Data Analytic"
    RASTER_FUNCTION_TEMPLATE = "Raster Function Template"
    GEOCODING_SERVICE = "Geocoding Service"
    GEOPROCESSING_SERVICE = "Geoprocessing Service"
    NETWORK_ANALYSIS_SERVICE = "Network Analysis Service"
    ORTHOMAPPING_PROJECT = "Orthomapping Project"
    ORTHOMAPPING_WORKSPACE = "Orthomapping Workspace"
    SOLUTION = "Solution"
    STYLE = "Style"
    FORM = "Form"
    INSIGHTS_WORKBOOK = "Insights Workbook"
    INSIGHTS_MODEL = "Insights Model"
    INSIGHTS_PAGE = "Insights Page"
    IMAGE_COLLECTION = "Image Collection"
    SERVICE_DEFINITION = "Service Definition"
    CODE_SAMPLE = "Code Sample"
    WORKFLOW_MANAGER_SERVICE = "Workflow Manager Service"
    RELATIONAL_DATABASE_CONNECTION = "Relational Database Connection"
    CSV_COLLECTION = "CSV Collection"
    FILE_GEODATABASE = "File Geodatabase"
    GROUP = "Group"
    LAYER = "Layer"
    CONTENT = "Content"
