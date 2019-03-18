import matplotlib.pyplot as plt
fn = 'loss.txt'
lines = open(fn).readlines()

y = list()
for line in lines:
	y.append(float(line.rstrip('\r\n')))
	
plt.plot(y)
