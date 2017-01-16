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
                logging.info('Now processing: %s', data_txt_path)
                df = pd.read_table(data_txt_path, sep=':', names=df_head)
                logging.debug('raw data:------------------------------- ')
                logging.debug(df[['lon','lat']][0:50])
                # TODO: 采用直接删除重复行法(仅保留第一行)有点武断.
                # 可以考虑先得出是否重复行的bool数组,然后对数组分析,
                # 如果连续较多重复行,则全部删去(不保留第一行),若较少则保留
                df = df.drop_duplicates(['lon','lat'])
                # 使用了drop_duplicates函数删除重复行,提出无效的车辆静止时的数据
                # 可能存在问题:当车辆实际运行过程中,轨迹存在相同的GPS坐标时,第二个会被误删去,不过影响不大
                logging.debug('drop duplicates:-----------')
                logging.debug(df[['lon', 'lat']][0:50])
                logging.debug('remained df length is: %d' % len(df))
                logging.debug('--------------------------------------------------------------------------\n\n')

                if len(df) < 50:  # 剩余有效数据太少,直接忽略
                    break
                # 保存df到文件,csv格式,通用性更好
                head1, day = os.path.split(root)
                head2, month = os.path.split(head1)
                head3, vehicle = os.path.split(head2)
                csv_path = os.path.join(my_config.new_data_path, vehicle)
                if not os.path.exists(csv_path):
                    os.mkdir(csv_path)  # 以车辆编号新建文件夹
                csv_path = os.path.join(csv_path, month+day+'.csv')

                df.to_csv(csv_path, header=False)  # 不储存说明头
                # df.to_csv(csv_path)  # 储存说明头

            # if files:
            #     break  # 测试用,只针对第一个文件夹做测试
        break  # 测试用,只针对第一个文件夹做测试
