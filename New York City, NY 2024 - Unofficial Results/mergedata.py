#Purpose of this file is for merging the geospatial ED data with the voting data

#Sourcing the venv
cd "New York City, NY 2024 - Unofficial Results"
source 'venv/bin/activate' 
pip install geopandas
ipython
import pandas as pd
import os
import geopandas as gpd

#Import Election data
E_data = pd.read_csv("precincts24.csv")
E_data = E_data.query("ED != 'Total'") #Remove Total rows
def number_convert(x):
    if len(str(x)) == 1:
        return("00"+str(x))
    if len(str(x)) == 2:
        return("0"+str(x))
    if len(str(x)) == 3:
        return(str(x))
E_data["ADED"] =  #######LEft here

#Import Shapefile data
gdf = gpd.read_file("nyed_24c")