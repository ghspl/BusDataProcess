#!/usr/bin/python2
# -*- coding: utf-8 -*-

import pandas as pd
import os
import my_config
import preprocess.preprocess_util


# df_head = []
# for line in open(my_config.data_header_path, 'r'):
#     line = line.rstrip()
#     df_head.append(line)
# df_head = df_head[0:50]
# print repr(df_head)

df_head = ['iindex', 'lon', 'lat', 'gpstime', 'gpsvelocity', 'northangle', 'vehstatus', 'alarmcode', 'orilon', 'orilat',
           'altitude', 'mile', 'fuel', 'enginetime', 'enginespeed', 'col14', 'col15', 'liquidtemper', 'voltage',
           'insfuel', 'edrspeed', 'oilpressure', 'airpressure', 'torquepercent', 'vehsignalstatus', 'speedfrom',
           'fueltank', 'overspeedalarm', 'col27', 'pedalpos', 'obuvolt', 'enginewatertemper', 'oiltemper',
           'influxtemper', 'dooropen', 'col34', 'col35', 'driverid', 'col37', 'systime', 'soc', 'current', 'volt',
           'col42', 'gears', 'col44', 'col45', 'col46', 'col47', 'col48', 'col49']

path = r'E:\data\newdata\110693470937697430214'
file_path = os.path.join(path, '0901.csv')
df = pd.read_csv(file_path, names=df_head)
# print df
# df.columns = df_head
# print(df[['lon', 'lat', 'gpstime']])
# print df.gpstime
df['time'] = df['gpstime'].apply(preprocess.preprocess_util.gpstime2bj)
# print(df[['lon', 'time']])

from matplotlib import pyplot as plt
plt.figure()
# print (df.iindex >= 192) & (df.iindex <= 462)
i1 = 192
i2 = 330
x = df[(df.iindex >= i1) & (df.iindex <= i2)]['lon']
y = df[(df.iindex >= i1) & (df.iindex <= i2)]['lat']
print len(df), len(x)
plt.scatter(x/600000, y/600000)
plt.show()
