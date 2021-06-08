# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 15:26
# @Author  : tangxl
# @FileName: settings.py
# @Software: PyCharm
"""
全局变量，包括各个窗口的位置和大小
"""

# 横坐标左右，纵坐标上下
big_window_size = [2400, 1800]

sub_window_size = [720, 720]
sub_window_loc_lu = [160, 140]
sub_window_loc_ru = [1000, 140]
sub_window_loc_ld = [160, 960]
sub_window_loc_rd = [1000, 960]

file_txt_loc = [160, 40]
file_txt_size = [200, 60]
file_name_loc = [file_txt_loc[0]+file_txt_size[0], file_txt_loc[1]]
file_name_size = [sub_window_loc_ru[0]+sub_window_size[0]-file_name_loc[0], file_txt_size[1]]

label_fixsize = [400, 40]
title_dis = [(sub_window_size[0]-label_fixsize[0])/2, sub_window_size[1]+20]

# right_bound = 2030

quit_loc = [1920, 45]
button_vertical_dis = 80
start_button_loc = [quit_loc[0], 240]
button_size = [300, 60]
# square_size = 40
