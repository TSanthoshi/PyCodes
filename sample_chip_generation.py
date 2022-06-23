# -*- coding: utf-8 -*-
"""

@author: santhoshi_t
"""

import glob, rasterio, os
from gdal import Translate


tile_size_x = 1024
tile_size_y = 1024


path1='</path/to/folder/containing/input/images>'
path2='</path/to/folder/to/write/output/images>'


inimgfiles = glob.glob(path1)

outtif_path = os.path.join(path2)

for imgfile in inimgfiles:
    dfimg = rasterio.open(imgfile)
    xsize = dfimg.width
    ysize = dfimg.height
    outtifname = imgfile[:-4]
    for i in list(range(0, xsize - tile_size_x, tile_size_x)) + [xsize - tile_size_x-1]:
        for j in list(range(0, ysize - tile_size_y, tile_size_y)) + [ysize - tile_size_y-1]:
            outfile = outtifname + str(i) + "_" + str(j)
            outtiftile = outfile + ".tif"
            outtiftilewpath = os.path.join(outtif_path, outtiftile)
            if not os.path.exists(outtiftilewpath):
                out=Translate(destName=outtiftilewpath, srcDS=imgfile, format='GTIFF', srcWin=[i, j, tile_size_x, tile_size_y])
                out=None