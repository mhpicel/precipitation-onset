import os
from datetime import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib import patheffects
from netCDF4 import Dataset as netcdf_dataset
import numpy as np
from scipy import interpolate
from siphon.catalog import TDSCatalog
from netCDF4 import num2date
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import patheffects
from netCDF4 import Dataset
import numpy as np
from scipy import interpolate
from siphon.catalog import TDSCatalog

nc = netcdf_dataset('goes_data.nc','r')

x = nc.variables['x'][:]
y = nc.variables['y'][:]
z = nc.variables['CMI_C13'][:]
sat = nc.variables['CMI_C13']


proj_var = nc.variables[nc.variables['CMI_C13'].grid_mapping]

globe = ccrs.Globe(ellipse='sphere', semimajor_axis=proj_var.semi_major_axis,
                      semiminor_axis=proj_var.semi_minor_axis)
"""

# proj_var.grid_mapping_name = 'geostationary'

proj = ccrs.Geostationary(central_longitude=proj_var.longitude_of_projection_origin22,
                          globe=globe)
"""

proj = ccrs.Mercator(central_longitude=proj_var.longitude_of_projection_origin, 
                     latitude_true_scale=proj_var.latitude_of_projection_origin,
                     globe=globe)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines(resolution='10m', color='black')
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor='black')
ax.add_feature(cfeature.BORDERS, linewidth=2, edgecolor='black')


for im in ax.images:
    im.remove()
ax.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper', cmap='Greys')
plt.show()
plt.close()

