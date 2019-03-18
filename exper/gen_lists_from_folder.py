import os

fnames = os.listdir("/data1/bzhang/dataset/oppo_dataset/Supervisely_img_jpg/")
fnames = sorted(fnames)
f = open('lists_super.txt', 'w+')
for fname in fnames:
	f.write(fname)
	f.write('\n')
	
f.close()