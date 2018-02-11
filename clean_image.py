#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 01:23:01 2018

@author: deepmind
"""

#to convert color jpeg to grey scale
import cv2
import glob
import numpy as np
import pandas as pd
import ntpath

df_pics_raw = []
lfiles = glob.glob('pics-raw/p2/**/**/*.tif')+glob.glob('pics-raw/**/**/**/*.tif')
lfiles = glob.glob('pics-raw/pA/**/**/*.tif')
lfiles += glob.glob('pics-raw/pB1/**/**/*.tif')
lfiles += glob.glob('pics-raw/pB2a/**/**/*.tif')
lfiles

for iPath in lfiles:
    print(iPath)

    try:
        image = cv2.imread(iPath)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        abssum = np.sum(np.abs(gray_image-np.roll(gray_image,1)))
        
        dFname = {'fpath':iPath,'dir':ntpath.dirname(iPath),'fname':ntpath.basename(iPath),'abssum':abssum}
        df_pics_raw.append(dFname)
    except:
        print('error',iPath)
    



df_pics = pd.DataFrame(df_pics_raw)

df_pics = df_pics.sort_values(['dir','abssum'])
#df_pics.groupby('dir').head(1)
#df_pics.groupby('dir').tail(1)

for ig, dfg in df_pics.groupby('dir'):
    for idf in dfg.head(1).to_dict('records'):
        try:
            ipath_tgt = 'pics-best/'+idf['fpath'].replace('/','-').replace('tif','jpg')
            image = cv2.imread(idf['fpath'])
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#            cv2.imwrite(ipath_tgt,gray_image)
            cv2.imwrite(ipath_tgt,image)
        except:
            print('error',iPath)
    
for ig, dfg in df_pics.groupby('dir'):
    for idf in dfg.tail(1).to_dict('records'):
        try:
            ipath_tgt = 'pics-worst/'+idf['fpath'].replace('/','-').replace('tif','jpg')
            image = cv2.imread(idf['fpath'])
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#            cv2.imwrite(ipath_tgt,gray_image)
            cv2.imwrite(ipath_tgt,image)
        except:
            print('error',iPath)

