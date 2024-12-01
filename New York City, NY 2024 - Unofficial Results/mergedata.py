#Purpose of this file is for merging the geospatial ED data with the voting data

#Sourcing the venv
cd "New York City, NY 2024 - Unofficial Results"
source 'venv/bin/activate' 
pip install geopandas
ipython
import pandas as pd
import geopandas as gpd

#Import Election data
E_data = pd.read_csv("precincts24.csv")
E_data = E_data.query("ED != 'Total'") #Remove Total rows

#Import Shapefile data
gdf = gpd.read_file("nyed.shp")