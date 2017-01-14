#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
程序的配置信息:
- 原始数据存储位置
-
"""

import os

busdata_par_path = r'C:\Users\Zhe Zhang\Documents\busdata'
busdata_folder = 'data'
busdata_path = os.path.join(busdata_par_path, busdata_folder)
# print busdata_path
new_data_path = os.path.join(busdata_par_path, 'newdata')
data_header_path = os.path.join(busdata_path, 'header.txt')