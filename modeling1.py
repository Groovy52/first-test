# import Module
import os
import cv2
import glob
import json
import timeit
import numpy as np
from random import *
#import tensorflow as tf
from patchify import patchify
import matplotlib.pyplot as plt
import imgaug.augmenters as iaa
from collections import OrderedDict

# make forlder
base_path = 'C:\\Users\\tndus\\workspace\\DIP\\project'
ori_path='DIP/data/18-40-02-02 (SLA).jpg' #원본 이미지
lbl_img_path='DIP/labelled_data/18-40-02-02 (SLA)_re_image.png' #원본 labelled 이미지

fnr_path='DIP/data/aug/remove_lt.jpg' #글씨 제거 이미지 

#Data Path
DIP_path=os.path.join(base_path,'DIP')
data_path = os.path.join(DIP_path, 'data')
lbl_path = os.path.join(DIP_path, 'labelled_data')

# 원본이미지 어그멘테이션 폴더 
data_aug_path = os.path.join(data_path,'aug')
aug_ver1_path = os.path.join(data_aug_path,'ver_1')
aug_ver2_path = os.path.join(data_aug_path,'ver_2')
aug_patch_path = os.path.join(aug_ver1_path,'patches')
aug2_patch_path = os.path.join(aug_ver2_path,'patches')

# 라벨이미지 어그멘테이션 폴더 
lbl_aug_path = os.path.join(lbl_path,'aug')
lbl_aug_ver1_path = os.path.join(lbl_aug_path,'ver_1')
lbl_aug_ver2_path = os.path.join(lbl_aug_path,'ver_2')
lbl_aug_patch_path = os.path.join(lbl_aug_ver1_path,'patches')
lbl_aug2_patch_path = os.path.join(lbl_aug_ver2_path,'patches')

# json 폴더 
json_path_ver1 = os.path.join(aug_ver1_path,'json')
json_path_ver2= os.path.join(aug_ver2_path,'json')

def mkfolder(folder):
    
    for j in range(len(folder)):
        if not os.path.exists(folder[j]):
            os.makedirs(folder[j])
  
'''
data_path, train_path는 string 타입의 path
mkfolder안에 입력할 값 = list 타입
'''

fold_list = [DIP_path,data_path,lbl_path,
             data_aug_path,aug_ver1_path,aug_ver2_path,aug_patch_path,aug2_patch_path,
            lbl_aug_path,lbl_aug_ver1_path,lbl_aug_ver2_path,lbl_aug_patch_path,lbl_aug2_patch_path ,
             json_path_ver1, json_path_ver2]

mkfolder(fold_list)