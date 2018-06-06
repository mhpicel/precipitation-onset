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

nc = netcdf_dataset('/home/scarani/Desktop/goes.nc','r')

x = nc.variables['x'][:]
y = nc.variables['y'][:]
z = nc.variables['CMI_C13'][:]
sat = nc.variables['CMI_C13']


proj_var = nc.variables[nc.variables['CMI_C13'].grid_mapping]

globe = ccrs.Globe(ellipse='sphere', semimajor_axis=proj_var.semi_major_axis,
                      semiminor_axis=proj_var.semi_minor_axis)
"""
proj = ccrs.Geostationary(globe=globe)

line_color = 'white'

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines(resolution='10m', color=line_color)
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor=line_color)
ax.add_feature(cfeature.BORDERS, linewidth=2, edgecolor=line_color)
ax.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper', cmap='Greys')



plt.show()


for im in ax.images:
    im.remove()
    im = ax.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper')
plt.show()
plt.close()
"""


if proj_var.grid_mapping_name == 'lambert_conformal_conic':
    proj = ccrs.LambertConformal(central_longitude=proj_var.longitude_of_central_meridian,
                                 central_latitude=proj_var.latitude_of_projection_origin,
                                 standard_parallels=[proj_var.standard_parallel],
                                 globe=globe)

else:
    proj = ccrs.Mercator(central_longitude=proj_var.longitude_of_projection_origin, 
                         latitude_true_scale=proj_var.latitude_of_projection_origin,
                         globe=globe)


line_color = 'white'

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines(resolution='10m', color=line_color)
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor=line_color)
ax.add_feature(cfeature.BORDERS, linewidth=2, edgecolor=line_color)
ax.imshow(z, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper', cmap='Greys')


# Plot text
#plt.title('GOES 16: '+ str(channel_title[int(channel)+1]), fontsize=20)

# Make the text stand out even better using matplotlib's path effects
#plt.savefig(savelocation + timestamp.strftime('%Y%m%d%H%M_') + 'ch-' + str(chno) + '.png', bbox_inches = 'tight', dpi = 300)
plt.show()
plt.close()