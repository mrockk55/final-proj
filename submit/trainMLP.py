import sys
import csv
import math
import random
import cPickle as pickle
import matplotlib.pylab as plt

"""trainMLP.py
	Trains Neural network of dimension 2-5-4
	over the given training data for provided number 
	of iterations
	@Author : Mayur Sanghavi
	@Author : Lee Avital
	@Version : 1.0 1st May, 2014
"""

#Sigmoid function 
def sigmoid(x):
	return 1/(1 + 1/(math.e**x))

#Calculate SSE and Delta for o/p layer
def SSE(d, output):
	
	act = d[2] -1 
	asgn = output.index(max(output))
	actual = [0.0, 0.0, 0.0, 0.0]
	actual[int(act)] = 1.0
	d = []
	err = 0.0
	for i in range(4):
	#Delta for o/p nodes
		d.append((actual[i] - output[i])*output[i]*(1-output[i]))
		err = err + ((actual[i] - output[i])**2)
	#Append SSE
	d.append(err)
	return d
	
	
#Trains NN for given epochs
def train():
	file1 = open(sys.argv[1])
	str = csv.reader(file1)
	#read data
	Data = []
	for s in str:
		Data.append([float(s[0]), float(s[1]), float(s[2])])
	weight = []
	random.seed()
	wt = []
	#Assign random weights
	for i in range(3):
		w = []
		for j in range(5):
			w.append(random.uniform(-1.0, 1.0))
		wt.append(w)
	weight.append(wt)
	wt = []
	for i in range(6):
		w = []
		for j in range(4):
			w.append(random.uniform(-1.0, 1.0))
		wt.append(w)
	weight.append(wt)
	#To store points for plot
	x = []
	y = []
	#Start training
	for i in range(int(sys.argv[2])):
		#For each row
		
		err = 0.0 
		
		for d in Data:
			#Delta for o/p layer
			delta = [0.0,0.0,0.0,0.0]
			#Delta for hidden layer
			delta1 = [0.0, 0.0, 0.0, 0.0, 0.0]
		
			#Calculate values
			input0 = [float(d[0]), float(d[1]), 1.0]
			input1 = []#Hidden outputs
			
			#Hidden Layer
			for l in range(5):
				temp = 0.0
				for n in range(3):
					temp += (input0[n]*weight[0][n][l])
				input1.append(sigmoid(temp))
			#bias
			input1.append(1.0)
			
			assigned = []#outputs
			#Output Layer
			for l in range(4):
				temp = 0.0
				for n in range(6):
					temp += (input1[n]*weight[1][n][l])
				assigned.append(sigmoid(temp))
			
			#Delta of output layer
			delta = SSE(d, assigned)
			
			#SSE
			err += delta[4]
		
			#Delta for hidden layer
			for l in range(5):
				temp = 0.0
				for n in range(4):
					temp += delta[n] * weight[1][l][n]
				delta1[l] = (temp*input1[l]*(1-input1[l]))
			
			#update weights
			#i/p to hidden
			for l in range(3):
				for n in range(5):
					weight[0][l][n] += 0.1 * delta1[n]* input0[l]
			
			#hidden to o/p
			for l in range(6):
				for n in range(4):
					weight[1][l][n] += 0.1 * delta[n]* input1[l]
		#Append SSE
		y.append(err)
		x.append(i)
		#Save weights
		if(i==0):
			pickle.dump(weight,open('0MLP.p','wb'))
		if(i==9):
			pickle.dump(weight,open('10MLP.p','wb'))
		elif(i==99):
			pickle.dump(weight,open('100MLP.p','wb'))
		elif(i==999):
			pickle.dump(weight,open('1000MLP.p','wb'))
	pickle.dump(weight,open('maxMLP.p','wb'))
	#Plot SSE vs Epoch
	plt.xlabel('Epochs')
	plt.ylabel('Sum of Squared Errors')
	plt.plot(x,y,'b')
	plt.show()
			
	

def main():
	if(len(sys.argv)<3):
		print 'Usage : >python trainMLP.py train_Data.csv [no. of epochs]'
	else:
		train()

if __name__ == '__main__':
	main()
