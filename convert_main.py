
#来自 如何使用Python处理HDF格式数据 https://cloud.tencent.com/developer/article/1471183

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm, colors

import seaborn as sns
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

from pyhdf.SD import SD, SDC

sns.set_context('talk', font_scale=1.3)

data = SD('LISOTD_LRMTS_V2.3.2014.hdf', SDC.READ)
lon = data.select('Longitude')
lat = data.select('Latitude')
flash = data.select('LRMTS_COM_FR')

# 设置colormap
collev= ['#ffffff', '#ab18b0', '#07048f', '#1ba01f', '#dfdf18', '#e88f14', '#c87d23', '#d30001', '#383838']
levels = [0, 0.01, 0.02, 0.04, 0.06, 0.1, 0.12, 0.15, 0.18, 0.2]
cmaps = colors.ListedColormap(collev, 'indexed')
norm = colors.BoundaryNorm(levels, cmaps.N)

proj = ccrs.PlateCarree()

fig, ax = plt.subplots(figsize=(16, 9), subplot_kw=dict(projection=proj))
print('125')

LON, LAT= np.meshgrid(lon[:], lat[:])

con = ax.contourf(LON, LAT, flash[:, :, 150], cmap=cmaps, norm=norm, levels=levels, extend='max')

#cb = fig.colorbar(con, shrink=0.75, pad=0.02)
#cb.cmap.set_over('#000000')
#cb.ax.tick_params(direction='in', length=5)

ax.coastlines()

#ax.set_xticks(np.linspace(-180, 180, 5), crs=proj)
#ax.set_yticks(np.linspace(-90, 90, 5), crs=proj)

lon_formatter= LongitudeFormatter(zero_direction_label=True)
lat_formatter= LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
plt.show()

