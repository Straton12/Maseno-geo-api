import os
from django.contrib.gis.utilis import LayerMapping
from djanngo.contrib.gis.gdal import DataSource
from myapp.models import MyModel

mymodel_mapping = {
    'fid_field': 'FID_',
    'name': 'Name',
    'structure': 'Structure',
    'use': 'Use',
    'no_floors': 'No_floors',
    'rooms': 'Rooms',
    'capacity': 'Capacity',
    'stracture': 'Stracture',
    'x': 'x',
    'y': 'y',
    'geom': 'POINT',
}

def import_data(verbose=True):
    file = os.getcwd() + "myproject/Data/Data.gpkg"
    data_source = DataSource(file)
    data_layer =  data_source[0].name
    
    data_layer_mapping = LayerMapping(
        data, file, data_layer_mapping, layer = data_layer
        )
    data_layer_mapping.save(verbose=verbose)'''