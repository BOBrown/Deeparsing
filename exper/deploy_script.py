import numpy as np
import os
import sys
import argparse
import glob
import time
import cv2
import pdb

sys.path.append("../python/")
import caffe

def uint82bin(n, count=8):
    """returns the binary of integer n, count refers to amount of bits"""
    return ''.join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def labelcolormap(N):
    cmap = np.zeros((N, 3), dtype = np.uint8)
    cmap[0, 0] = 0
    cmap[0, 1] = 0
    cmap[0, 2] = 0
    
    cmap[1, 0] = 255
    cmap[1, 1] = 255
    cmap[1, 2] = 255
    
    return cmap

def convert_colormap(image, label, colormap, num_clc):
    height = image.shape[0]
    width = image.shape[1]
    label_resize = cv2.resize(label, (width, height), interpolation=cv2.INTER_NEAREST)
    img_color = np.zeros([height, width, 3], dtype=np.uint8)
    img_rgb   = np.zeros([height, width, 3], dtype=np.uint8)
    #img_rgb = image.copy()
    for idx in range(num_clc):
        img_color[label_resize==idx] = colormap[idx]
        img_rgb[label_resize==idx] = image[label_resize==idx]*0.5 + colormap[idx]*0.5
        
    return img_color, img_rgb

def parsing(model_proto,model_weight, data_path):
    num_cls = 2
    colormap = labelcolormap(num_cls)
    print "colormap",colormap
    #pdb.set_trace()
    caffe.set_mode_gpu()
    caffe.set_device(0)

    #pdb.set_trace()
    # Make classifier.
    mean = np.array([104.008, 116.669, 122.675])
    input_scale = 1.0
    raw_scale = 255.0
    channel_swap = [2,1,0]
    classifier = caffe.Classifier(model_proto, model_weight, mean=mean, input_scale=input_scale, raw_scale=raw_scale, channel_swap=channel_swap)    
    #pdb.set_trace()
    
    data_path_img = os.path.join(data_path,'img/')
    
    image_files = os.listdir(data_path_img)
	  
    for image_file in image_files:
      image_file_dir = data_path_img + image_file
     
      #pdb.set_trace()
      image = cv2.imread(image_file_dir)
      inputs = [caffe.io.load_image(image_file_dir)]
      predictions = classifier.predict(inputs)
      out = classifier.blobs['fc8_interp_argmax'].data
      out_label = np.array(out[0,0,:,:], dtype=np.uint8)
      out_label = out_label.T[::-1].transpose() 
      #or out_label = np.fliplr(out_label)
      im_color, img_rgb = convert_colormap(image, out_label, colormap, num_cls)
      name, ext = os.path.splitext(image_file)
      fn_out = os.getcwd() + '/result/' + name + '.png'
      print "color image saved in",fn_out
      cv2.imwrite(fn_out, im_color)
	  
      #pdb.set_trace()
      print fn_out
        
if __name__ == '__main__':
    if len(sys.argv)==4:
        parsing(sys.argv[1], sys.argv[2],sys.argv[3])
    else:
        print "Uage: deploy_script.py model_proto model_weight"