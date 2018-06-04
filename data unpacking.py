from datetime import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib import patheffects
from netCDF4 import Dataset
import numpy as np
from scipy import interpolate
from siphon.catalog import TDSCatalog


date = datetime.utcnow()
channel = 13 
idx = -2
region = 'Mesoscale-1'

"""
Open and return a netCDF Dataset object for a given date, channel, and image index
of GOES-16 data from THREDDS test server.
"""
cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/satellite/goes16/GOES16/'
             '{}/Channel{:02d}/{:%Y%m%d}/catalog.xml'.format(region, channel, date))
ds = cat.datasets[idx].remote_access(service='OPENDAP')                     
