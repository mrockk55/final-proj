import sys
import csv
import math
import random
import cPickle as pickle
import matplotlib.pylab as plt

def IG(data, attr, w):
	#print attr
	count = [0,0,0,0]
	left = [0,0,0,0]
	right = [0,0,0,0]
	for d in data:
		count[int(d[2])-1] += 1
		if(d[attr]<=w):
			left[int(d[2])-1] += 1
		else :
			right[int(d[2])-1] += 1
	total = sum(count)
	totalf = sum(left)
	totalr = sum(right)
	
	#print count
	#print total
	#Information Content
	IC = 0
	for c in count :
		if(c > 0):
			IC = IC - (c/float(total)) * math.log(c/float(total), 2)
	#print IC
	#Remainder(attr)
	remainl = 0
	remainr = 0
	for l in left:
		if(l>0):
			remainl = remainl - (l/float(totalf)) * math.log(l/float(totalf), 2)
	remainl = remainl * totalf / total
	#print remainl
	for r in right:
		if(r>0):
			remainr = remainr - (r/float(totalr)) * math.log(r/float(totalr), 2)
	remainr = remainr * totalr / total
	#print remainr
	#print (IC - remainl - remainr)
	return (IC - remainl - remainr)
	
	
def SSE(data, tree):
	err = 0.0
	correct = 0
	incorrect = 0
	for d in data:
		prob = [0.0,0.0,0.0,0.0]
		for t in tree:
			if d[t[0]] <= t[1]:
				if d[t[2]] <= t[3]:
					prob[t[6]-1] += t[7]
				else :
					prob[t[8]-1] += t[9]
			else:
				if d[t[4]] <= t[5]:
					prob[t[10]-1] += t[11]
				else:
					prob[t[12]-1] += t[13]
		for i in range(len(prob)):
			prob[i] = prob[i] / len(tree)
		actual = [0.0, 0.0, 0.0, 0.0]
		actual[int(d[2])-1] = 1.0
		
		for i in range(len(prob)):
			err = err + (prob[i] - actual[i])**2
	return err

def train():
	"""w1 = csv.writer(open('trees1.csv','wb'))
	w2 = csv.writer(open('trees10.csv','wb'))
	w3 = csv.writer(open('trees100.csv','wb'))
	w4 = csv.writer(open('treesMax.csv','wb'))"""
	x = []
	y = []
	file1 = open(sys.argv[1])
	str = csv.reader(file1)
	Data = []
	for s in str:
		Data.append([float(s[0]), float(s[1]), float(s[2])])
	Tree = []
	
	for i in range(int(sys.argv[2])):
		T = []
		random.seed()
		#Root node
		attr = []
		for j in range(6):
			attr.append(random.random())
		G = []
		for j in range(6):
			G.append(IG(Data,j/3,attr[j]))
		index = G.index(max(G))
		a1 = index/3
		w1 = attr[index]
		T.append(a1)
		T.append(w1)
		
		Datal = []
		Datar = []
		for d in Data:
			if d[a1] <= w1:
				Datal.append(d)
			else:
				Datar.append(d)
		
		#Left Child
		attr = []
		for j in range(6):
			attr.append(random.random())
		G = []
		for j in range(6):
			G.append(IG(Datal,j/3,attr[j]))
		index = G.index(max(G))
		a1 = index/3
		w1 = attr[index]
		T.append(a1)
		T.append(w1)
		"""
		Datall = []
		Datalr = []
		for d in Datal:
			if d[a1] <= w1:
				Datall.append(d)
			else:
				Datalr.append(d)	
		"""
		#Right Child
		attr = []
		for j in range(6):
			attr.append(random.random())
		G = []
		for j in range(6):
			G.append(IG(Datar,j/3,attr[j]))
		index = G.index(max(G))
		a1 = index/3
		w1 = attr[index]
		T.append(a1)
		T.append(w1)
		"""
		Datarl = []
		Datarr = []
		for d in Datar:
			if d[a1] <= w1:
				Datarl.append(d)
			else:
				Datarr.append(d)
		"""
		
		#l-l-l & l-l-r
		count1 = [0,0,0,0]
		count2 = [0,0,0,0]
		for d in Datal:
			
			if(d[int(T[2])]<=T[3]):
				count1[int(d[2]-1)] += 1
			else:
				count2[int(d[2]-1)] += 1
			
		val1 = count1.index(max(count1)) + 1
		prob1 = 0.0
		if sum(count1) > 0:
			prob1 = max(count1)/float(sum(count1))
		val2 = count2.index(max(count2)) + 1
		prob2 = 0.0
		if sum(count2) > 0:
			prob2 = max(count2)/float(sum(count2))
		T.append(val1)
		T.append(prob1)
		T.append(val2)
		T.append(prob2)		
		
		#l-r-l & l-r-r
		count1 = [0,0,0,0]
		count2 = [0,0,0,0]
		for d in Datar:
			
			if(d[int(T[4])]<=T[5]):
				count1[int(d[2]-1)] += 1
			else:
				count2[int(d[2]-1)] += 1
			
		val1 = count1.index(max(count1)) + 1
		prob1 = 0.0
		if sum(count1) > 0:
			prob1 = max(count1)/float(sum(count1))
		val2 = count2.index(max(count2)) + 1
		prob2 = 0.0
		if sum(count2) > 0:
			prob2 = max(count2)/float(sum(count2))
		T.append(val1)
		T.append(prob1)
		T.append(val2)
		T.append(prob2)
		#print T
		Tree.append(T)
		y.append(i)
		x.append(SSE(Data,Tree))
		if(i==0):
			pickle.dump(Tree,open('1Tree.p','wb'))
		elif(i==9):
			pickle.dump(Tree,open('10Tree.p','wb'))
		elif(i==99):
			pickle.dump(Tree,open('100Tree.p','wb'))
	pickle.dump(Tree,open('maxTree.p','wb'))
	plt.plot(y,x,'b')
	plt.show()
		
	

def main():
	if(len(sys.argv)<3):
		print 'Usage : >python trainDT.py train_Data.csv [no. of trees]'
	else:
		train()

if __name__ == '__main__':
	main()
