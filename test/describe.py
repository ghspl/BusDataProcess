#!/usr/bin/python2
# -*- coding: utf-8 -*-

import pandas as pd
import os
import my_config
import preprocess.preprocess_util

df_head = ['iindex', 'lon', 'lat', 'time', 'dist', 'spd']
path = r'E:\data'
file_path = os.path.join(path, '0901full.csv')
df = pd.read_csv(file_path, names=df_head)
#print df

print preprocess.preprocess_util.stats(df['dist']),
print preprocess.preprocess_util.stats(df['spd'])