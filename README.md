# Deeparsing Workshop
This is a human parsing project based on caffe tools.

This project is to parse human body and output the binary picture. The pixel of Human body is 255, and background is 0.
The running time of this code is 100ms/batch on 1080ti GPU.
 
The basic CNN backbone employs PSPNet. Technical details are in the paper: **[Pyramid Scene Parsing Network]**(https://arxiv.org/abs/1612.01105)


# Installation:
For installation, cuDNN version should less than cuDNN v4. If you use cuda8.0, then could not support cuDNN v4.

## Install matio:

download  matio-1.5.2.tar.gz https://sourceforge.net/projects/matio/files/matio/1.5.2/
>$ tar zxf matio-X.Y.Z.tar.gz 
         
>$ cd matio-X.Y.Z

>$ ./configure

>$ make

>$ make check

>$ sudo make install

## Install caffe:
>$ cd deeparsing-master 

>$ make -j32 && make pycaffe -j32

# How to use this project:
### (1) cd the exper dir:
>$ cd deeparsing-master/exper

### (2) download the weights and network files 
Link: https://pan.baidu.com/s/1h3oF0LUsv_6Ub-CLghKjEw CODE: i1ja

### (3) saved weights in the deeparsing-master/exper/config folder

>$ mv parsing_v2.caffemodel deeparsing-master/exper/config

>$ mv deploy_v2.prototxt deeparsing-master/exper/config

### (4) testing the dataset

>$ cd deeparsing-master/exper

>$ python test.py --data_dir "dir of test set" --gpu_id 0

### (5) looking into the resulting images

>$ cd deeparsing-master/exper/deeparsing

>$ ls 


# Other Scripts:
Many useful scripts for human parsing task are saved in the deeparsing-master/exper folder.

For examples:

convert_parsing_label.py  : convert the label of each image to another value

gen_lists_from_folder.py : get list file from the image folder

gen_train_val_from_lists.py : create train.txt and val.txt file from the list file, that is useful for training our models.

# Some Results:

![original img](https://raw.githubusercontent.com/BOBrown/deeparsing-master/master/results/2007_000480.jpg)

![parsing img](https://raw.githubusercontent.com/BOBrown/deeparsing-master/master/results/2007_000480.png)

![original img](https://raw.githubusercontent.com/BOBrown/deeparsing-master/master/results/997_20.jpg)

![parsing img](https://raw.githubusercontent.com/BOBrown/deeparsing-master/master/results/997_20.png)