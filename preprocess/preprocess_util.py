#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
数据预处理自定义工具函数
"""

import pandas as pd
import time

def systime2bj(unix_time):
    format = '%Y-%m-%d %H:%M:%S'
    time_array = time.localtime(unix_time/1000)  # 转换为秒级来处理
    dt = time.strftime(format, time_array)
    return dt


if __name__ == '__main__':
    unixtime = 1474238421303
    print systime2bj(unixtime)
