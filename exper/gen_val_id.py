import os

f = open('val.txt', 'r')
lines = f.readlines()
f.close()

f = open('val_id.txt', 'w+')
for line in lines:
	fn, ext = os.path.splitext((os.path.basename(line.strip('\n'))))
	f.write(fn)
	f.write('\n')
f.close()