import cv2
import os
import os.path
import sys
import numpy as np
import pdb
from PIL import Image  

label_map_supervisely ={0:0,
    1:1,
    2:1,
    3:1,
    }
    
label_map = {0:0,
    1:1,
    2:1,
    3:1,
    4:1,
    5:1,
    6:1,
    7:1,
    8:1,
    9:1,
    10:1,
    11:1,
    12:1,
    13:1,
    14:1,
    15:1,
    16:1,
    17:1
    }

label_map_lip = {0:0,
    1:1,
    2:1,
    3:1,
    4:1,
    5:1,
    6:1,
    7:1,
    8:1,
    9:1,
    10:1,
    11:1,
    12:1,
    13:1,
    14:1,
    15:1,
    16:1,
    17:1,
    18:1,
    19:1
    }
    
label_map_mul = {0:0,
    1:1,
    2:1,
    3:1,
    4:1,
    5:1,
    6:1,
    7:1,
    8:1,
    9:1,
    10:1,
    11:1,
    12:1,
    13:1,
    14:1,
    15:1,
    16:1,
    17:1,
    18:1,
    19:1,
    }


label_map_voc = {0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
    13:0,
    14:0,
    15:1,
    16:0,
    17:0,
    18:0,
    19:0,
    20:0,
    255:0
    }

label_map_show ={
  0:0,
  1:255
}
def get_file_list(root_path, ext):
    path_per_folder = {}
    for rt, dirs, files in os.walk(root_path):
        for f in files:            
            fname = os.path.splitext(f)
            #pdb.set_trace()
            if fname[-1] == "."+ext:
                if rt not in path_per_folder.keys():
                    path_per_folder[rt] = []
                path_per_folder[rt].append(os.path.join(rt, f))
    return path_per_folder



def cvt_label(input_path, output_root):
    img = cv2.imread(input_path, 0)
    sp = img.shape
    height = sp[0]
    width = sp[1]
    for y in range(0, height):
        for x in range(0, width):
            img[y, x] = label_map_show[img[y,x]]
    file_name = input_path.split(os.sep)[-1]
    output_path = os.path.join(output_root, file_name)
    print "export to %s" % output_path
    cv2.imwrite(output_path, img)

def cvt_label_voc(input_path, output_root):
    I = Image.open(input_path)
    I_array = np.array(I)
    sp = I_array.shape
    height = sp[0]
    width = sp[1]
    for y in range(0, height):
        for x in range(0, width):
            I_array[y, x] = label_map_voc[I_array[y,x]]
    file_name = input_path.split(os.sep)[-1]
    output_path = os.path.join(output_root, file_name)
    print "export to %s" % output_path
    cv2.imwrite(output_path, I_array)

def eport2files(file_list, output_folder):
    for key in file_list.keys():
        for file_path in file_list[key]:
            file_name_new = file_path.split(os.sep)[-1]
            file_path_new = output_folder + file_name_new
            if os.path.exists(file_path_new):
              print "exist:",file_path_new
              continue
            else:
              cvt_label(file_path, output_folder)


if __name__ == '__main__':
    if len(sys.argv)==4:
        file_list = get_file_list(sys.argv[1], sys.argv[3])
        eport2files(file_list, sys.argv[2])
    else:
        print "Uage: cvtParsingLabel.py root_folder output_folder ext"