IS project 2
Python files are:
trainMLP.py, trainDT.py, executeMLP.py, executeDT.py

Project write-up: Project2.pdf

Data folder contains the neural network and Decision Trees that can be used to test dat.

trainMLP.py : To train MLP netwrok
to run
>python trainMLP.py train_Data.csv [no. of epochs]

Generates the weight files for neural networks 0MLP.p, 10MLP.p, 100MLP.p, 1000MLP.p and 10000MLP.p . Also generates the learning curve for MLP and plots the input data.


executeMLP.py : To classify the data
to run
>python executeMLP.py test_Data.csv [maxMLP.p]
Takes test data and weights for neural network as input. Generates the class region and plot of input points. Also prints Recognition rate, profit and confusion matrix.


trainDT.py : To train Decision Trees
to run
>python trainDT.py train_Data.csv [Max no. of trees]

Generates the decision trees file for neural networks 0MLP.p, 10MLP.p, 100MLP.p, 1000MLP.p and 10000MLP.p . Also generates the learning curve for Decision Trees and plots the input data.


executeDT.py : To classify the data
to run
>python executeDT.py test_Data.csv [maxTree.p]
Takes test data and Decision Trees as input. Generates the class region and plot of input points. Also prints Recognition rate, profit and confusion matrix.