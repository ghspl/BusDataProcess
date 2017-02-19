#!/usr/bin/python2
# -*- coding: utf-8 -*-


import pandas as pd
import os
import my_config
import preprocess.preprocess_util
from datetime import datetime


# def haversine(lon1, lat1,lon2, lat2):
#     # 将十进制度数转化为弧度
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
#     # haversine公式
#     dlon = (abs(lon2 - lon1))/600000
#     dlat = (abs(lat2 - lat1))/600000
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a))
#     r = 6371 # 地球平均半径，单位为千米
#     return c * r * 1000
# 测试
# print haversine(110.0123, 23.32435,129.1344,25.5465)


df_head = ['iindex', 'lon', 'lat', 'gpstime', 'gpsvelocity', 'northangle', 'vehstatus', 'alarmcode', 'orilon', 'orilat',
           'altitude', 'mile', 'fuel', 'enginetime', 'enginespeed', 'col14', 'col15', 'liquidtemper', 'voltage',
           'insfuel', 'edrspeed', 'oilpressure', 'airpressure', 'torquepercent', 'vehsignalstatus', 'speedfrom',
           'fueltank', 'overspeedalarm', 'col27', 'pedalpos', 'obuvolt', 'enginewatertemper', 'oiltemper',
           'influxtemper', 'dooropen', 'col34', 'col35', 'driverid', 'col37', 'systime', 'soc', 'current', 'volt',
           'col42', 'gears', 'col44', 'col45', 'col46', 'col47', 'col48', 'col49']
path = r'E:\data\newdata\110693470937697430214'
file_path = os.path.join(path, '0901.csv')
df = pd.read_csv(file_path, names=df_head)
df['time'] = df['gpstime'].apply(preprocess.preprocess_util.gpstime2bj)
df['lon'] = df['lon']/600000
df['lat'] = df['lat']/600000


df2 = df[['iindex', 'lon','lat','time']]
df2['dist'] = 0.0
df2['speed'] = 0.0
for i in range(len(df2)):
    if i >0:
        lon1 = df2['lon'].iloc[i]
        lat1 = df2['lat'].iloc[i]
        lon2 = df2['lon'].iloc[i - 1]
        lat2 = df2['lat'].iloc[i - 1]
        df2['dist'].iloc[i] = preprocess.preprocess_util.distance4gps(lon1, lat1,lon2, lat2)
        df2['ctime'] =df2['time'].iloc[i] - df2['time'].iloc[i-1]
        df2['speed'].iloc[i] = (df2['dist'].iloc[i])/(preprocess.preprocess_util.ctime(df2['time'].iloc[i], df2['time'].iloc[i-1]))
#print df2

df2.to_csv('E:/data/0901full.csv')