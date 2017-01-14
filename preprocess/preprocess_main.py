#!/usr/bin/python2
# -*- coding: utf-8 -*-


"""
数据预处理: 包括遍历文件夹读取所有文件,判断数据有效性, 删除冗余数据, 有效数据存储
"""

import os
import logging
import sys
import pandas as pd

import my_config


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert os.path.exists(my_config.busdata_path)  # 判断原始数据文件夹是否存在
    if not os.path.exists(my_config.new_data_path):
        os.mkdir(my_config.new_data_path)
    df_head = []
    for line in open(my_config.data_header_path, 'r'):
        line = line.rstrip()
        df_head.append(line)
    df_head = df_head[0:50]
    # 遍历某个车的编号下的所有文件夹, 模式为月-日-txt文件
    data_dirs = os.listdir(my_config.busdata_path)
    logging.debug('dirs in data folder are: %s' % data_dirs)
    for cur_dir in data_dirs:
        work_path = os.path.join(my_config.busdata_path, cur_dir)  # 选取一个车的文件夹为工作文件夹
        for root, dirs, files in os.walk(work_path):
            for dbfile in files:
                data_txt_path = os.path.join(root, dbfile)
                logging.debug('Now processing: %s', data_txt_path)
                df = pd.read_table(data_txt_path, sep=':', names=df_head)
                print df[['lon','lat']][0:50]

        break  # 测试用,只针对第一个文件夹做测试
