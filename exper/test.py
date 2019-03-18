import numpy as np
import os
import sys
import argparse
import glob
import time
import cv2
from numba import jit

sys.path.append("/data1/bzhang/SEG/PSPNet-master/python/")
os.environ['GLOG_minloglevel'] = '2'
import caffe

def uint82bin(n, count=8):
    """returns the binary of integer n, count refers to amount of bits"""
    return ''.join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

@jit
def labelcolormap(N):
    cmap = np.zeros((N, 3), dtype = np.uint8)
    cmap[0, 0] = 0
    cmap[0, 1] = 0
    cmap[0, 2] = 0
    
    cmap[1, 0] = 255
    cmap[1, 1] = 255
    cmap[1, 2] = 255
    
    return cmap
    
@jit
def convert_colormap(image, label, colormap, num_clc):
    height = image.shape[0]
    width = image.shape[1]
    label_resize = cv2.resize(label, (width, height), interpolation=cv2.INTER_NEAREST)
    img_color = np.zeros([height, width, 3], dtype=np.uint8)
    #img_rgb = image.copy()
    for idx in range(num_clc):
        img_color[label_resize==idx] = colormap[idx]
        
    return img_color


def img_processing(image_file_dir, size):
  img_ori = cv2.imread(image_file_dir)
  image = cv2.resize(img_ori, (size,size))
  img = np.zeros((1,3,size,size))
  img[0,0,:,:] = image[:,:,0]-104.008
  img[0,1,:,:] = image[:,:,1]-116.669
  img[0,2,:,:] = image[:,:,2]-122.675
 
  return img_ori,img


def parsing(model_proto,model_weight, ID, data_path):
    num_cls = 2
    colormap = labelcolormap(num_cls)

    #pdb.set_trace()
    caffe.set_mode_gpu()
    caffe.set_device(int(ID))

    #pdb.set_trace()
    # Make classifier.
    net = caffe.Net(model_proto,model_weight,caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', np.array([104.008,116.669,122.675])) 
    transformer.set_raw_scale('data', 255) 
    transformer.set_channel_swap('data', (2,1,0)) 
    
    
    #pdb.set_trace()
    data_path_img = os.path.join(data_path,'img/')
    
    image_files = os.listdir(data_path_img)

    if not len(image_files):
      print "[Deeparsing log] no images in the corresponding dir!"
    for image_file in image_files:
      image_file_dir = data_path_img + image_file
      
      
      
      #pdb.set_trace()
      start = time.time()
      img_ori,im = img_processing(image_file_dir,513)
      #im = caffe.io.load_image(image_file_dir)
      #net.blobs['data'].data[...] = transformer.preprocess('data',im)
      net.blobs['data'].data[...] = im
      predictions = net.forward()
      print("Done in %.2f s." % (time.time() - start))
      out = net.blobs['fc8_interp_argmax'].data
      out_label = np.array(out[0,0,:,:], dtype=np.uint8)
      out_label = out_label.T[::-1].transpose() 
      out_label = np.fliplr(out_label)
      im_color = convert_colormap(img_ori, out_label, colormap, num_cls)
      name, ext = os.path.splitext(image_file)
      fn_out = os.getcwd() + '/deeparsing/' + name + '.png'
      print "color image saved in",fn_out
      cv2.imwrite(fn_out, im_color)
	    
      #pdb.set_trace()
      #print fn_out
        
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--data_dir", required=True, help="name of trained model")
    ap.add_argument("-n", "--gpu_id", required=True, help="name of trained model")
    args = vars(ap.parse_args())
    
    
    if len(sys.argv)==5:
        parsing("./config/deploy_v2.prototxt", "./config/parsing_v2.caffemodel",args["gpu_id"],args["data_dir"])
        #parsing("./config/deploy_v3.prototxt", "./config/parsing_v3.caffemodel",args["gpu_id"],args["data_dir"])
    else:
        print "Uage: test.py --data_dir --gpu_id"