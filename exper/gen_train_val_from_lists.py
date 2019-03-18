import os
import random

f = open('lists_super.txt', 'r')
lines = f.readlines()
f.close()

for i in range(50):
	random.shuffle(lines)

#f = open('lists_shuffle.txt', 'w+')
#for line in lines:
#	#line = line.strip('\n')
#	f.write(line)
#	#f.write('\n')
#f.close()

length = len(lines)
print length

l_train = int(length*0.98)
lines_train = lines[0:l_train]
lines_val = lines[l_train:length]

f = open('train_super.txt', 'w+')
for line in lines_train:
	fn, ext = os.path.splitext((os.path.basename(line.strip('\n'))))
	#str = '/JPEGImages/' + fn + '.jpg' + ' ' + '/SegmentationClassAug_clothes/' + fn + '.png'
	str = '/JPEGImages/{}.jpg /SegmentationClassAug_2cls/{}.png'.format(fn, fn)
	f.write(str)
	f.write('\n')
f.close()


f = open('val_super.txt', 'w+')
for line in lines_val:
	fn, ext = os.path.splitext((os.path.basename(line.strip('\n'))))
	#str = '/JPEGImages/' + line.strip('\n') + ' ' + '/SegmentationClassAug/' + line.strip('\n')
	str = '/JPEGImages/{}.jpg /SegmentationClassAug_2cls/{}.png'.format(fn, fn)
	f.write(str)
	f.write('\n')
f.close()