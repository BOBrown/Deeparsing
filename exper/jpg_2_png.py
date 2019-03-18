from PIL import Image
import glob
import os
import cv2
import shutil


img_root="/data1/bzhang/dataset/oppo_dataset/JPEGImage_Total/"
output_dir = "/data1/bzhang/dataset/oppo_dataset/JPEGImages/"

def file_extension(path): 
  return os.path.splitext(path)[1] 
  
def file_name(path): 
  return os.path.splitext(path)[0] 
  
def jpg2png(img_root):
    img_files = os.listdir(img_root)
    print img_files
    num = 0
    for img_file in img_files:
        mix_file_dir = img_root + img_file
        im = Image.open(mix_file_dir)
        bname=os.path.basename(img_file)
        out_filename=bname[:-3]+'jpg' 
        im.save(output_dir+out_filename)

        num = num + 1
        #break

        print (num)


jpg2png(img_root)

