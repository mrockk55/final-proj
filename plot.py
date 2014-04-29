import sys
import csv
import math
import matplotlib.pylab as plt
import numpy as np


def main():
	file1 = open(sys.argv[1])
	str = csv.reader(file1)
	for s in str:
		x = float(s[0])
		y = float(s[1])
		c = float(s[2])
		if(c == 1):
			#bolt
			plt.plot(x,y,'rs')
		elif(c == 2):
			#nut
			plt.plot(x, y, 'bo')
		elif(c == 3):
			#ring
			plt.plot(x, y, 'go')
		else:
			#scrap
			plt.plot(x, y, 'k^')
		plt.xlabel("Rot.")
		plt.ylabel("Ecc")
	plt.show()
		

if __name__ == '__main__':
	main()