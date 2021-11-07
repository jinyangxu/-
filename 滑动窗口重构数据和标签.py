# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:05:50 2021

@author: atr
"""

import os
import pandas as pd
load_path = "F://MRI//自闭症//数据集//aal//ABIDE_pcp//cpac//nofilt_noglobal//"
files = os.listdir(load_path)

"""
这部分的功能是将每个.1D文件的数据通过（N-L）/10滑动窗口,转化成10个长度为60的数据
其中N是时间序列的总长度，L是窗口的长度，本次实验所有的窗口长度都设置为60
"""
def newdata(files):
    for file in (files):
    file_name, file_exp = os.path.splitext(file) #分离文件名和扩展名
    data = pd.read_table(load_path+file)
    data = np.array(data)
    S = []
    N = data[:,1].size
    L = 60
    P = (N-L)/10
    p = int (P)
    print(p)
    for j in range(10):
        S.append(data[j*p:(j)*p+L])
    np.save("F://MRI//自闭症//数据集//test_1//"+file_name+".npy",np.array(S))

c = pd.read_csv("F://MRI//自闭症//数据集//aal//ABIDE_pcp//Phenotypic_V1_0b_preprocessed1.csv")    

"""
先将每个受试者的文件名和对应的标签打包，然后构建标签集
"""
def getlabels(c,files):
    key = []
    value = []
    for i in range(1112):
        key.append(c['FILE_ID'][i])
        value.append(c['DX_GROUP'][i])
    dict1 = dict(zip(key,value))#将文件名和便签ID通过zip打包映射
    label = []
    for file in (files):
        file_name, file_exp = os.path.splitext(file) #分离文件名和扩展名
        label.append(dict1[file_name.strip('_rois_aal')])
    label = np.array(label)
    np.save("F://MRI//自闭症//数据集//label"+".npy",label)
    
    
    
    
    
    
    
    
    