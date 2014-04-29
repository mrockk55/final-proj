import sys
import csv
import math
import random
import matplotlib.pylab as plt
import numpy as np

def train():
	w1 = csv.writer(open('trees1.csv','wb'))
	w2 = csv.writer(open('trees10.csv','wb'))
	w3 = csv.writer(open('trees100.csv','wb'))
	w4 = csv.writer(open('treesMax.csv','wb'))
	x = []
	y = []
	for i in range(int(sys.argv[2])):
		random.seed()
		nodes = []
		weights = []
		for j in range(7):
			nodes.append(random.randint(0,1))
			weights.append(random.random())
		count = [[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0],
				[0,0,0,0]]
		
		
		file1 = open(sys.argv[1])
		str = csv.reader(file1)
		#Train Over Data File
		#Dpeth of Tree : 4
		for s in str:
			if(float(s[nodes[0]])<=weights[0]):
				if(float(s[nodes[1]])<=weights[1]):
					if(float(s[nodes[3]])<=weights[3]):
						count[0][int(s[2])-1]+=1
					else:
						count[1][int(s[2])-1]+=1
				else:
					if(float(s[nodes[4]])<=weights[4]):
						count[2][int(s[2])-1]+=1
					else:
						count[3][int(s[2])-1]+=1
			else:
				if(float(s[nodes[2]])<=weights[2]):
					if(float(s[nodes[5]])<=weights[5]):
						count[4][int(s[2])-1]+=1
					else:
						count[5][int(s[2])-1]+=1
				else:
					if(float(s[nodes[6]])<=weights[6]):
						count[6][int(s[2])-1]+=1
					else:
						count[7][int(s[2])-1]+=1
		file1.close()
		w= nodes + weights
		sse = 0
		for j in range(8):
			w.append(count[j].index(max(count[j]))+1)
			sse = sse + (sum(count[j]) - max(count[j]))**2
		if(i==0):
			w1.writerow(w)
		if(i < 10):
			w2.writerow(w)
		if(i < 100):
			w3.writerow(w)
		if(i < int(sys.argv[2])):
			w4.writerow(w)
		x.append(sse)
		y.append(i)
	plt.plot(y,x,'b')
	plt.show()

def main():
	if(len(sys.argv)<3):
		print 'Usage : >python trainDT.py train_Data.csv [no. of trees]'
	else:
		train()

if __name__ == '__main__':
	main()
