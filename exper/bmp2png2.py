# !/usr/bin/env python
# coding=utf-8


import glob
import os
import cv2
from PIL import Image

def file_extension(path): 
  return os.path.splitext(path)[1] 
  
def file_name(path): 
  return os.path.splitext(path)[0] 
  
image_root= "/data1/bzhang/dataset/oppo_dataset/Supervisely_img/"
outputimg = "/data1/bzhang/dataset/oppo_dataset/Supervisely_img_jpg/"

def bmp2jpg(image_root):
    image_files = os.listdir(image_root)
    print image_files
    num = 0
    for image_file in image_files:
        image_file_dir = image_root + image_file
        
        print image_file_dir
        im = Image.open(image_file_dir)
        im_2_rgb =im.convert("RGB")
        
        bname=os.path.basename(image_file)
        out_filename=bname[:-3]+'jpg' 
        
        print "out_filename:",out_filename
        
        save_image_file_dir1 = outputimg + out_filename
        
        print "save_image_file_dir1:",save_image_file_dir1
        im_2_rgb.save(save_image_file_dir1)
        num = num + 1
        #break

    print (num)


bmp2jpg(image_root)


