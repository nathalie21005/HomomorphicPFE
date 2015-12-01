#import matplotlib.pyplot as mpl
#Sfrom numpy import * 
import os


file_data = os.getcwd() + "D:\\ProjectPFE\\faces\\faceS.txt"
F = open('D:\\ProjectPFE\\faces\\faceS', 'r')
DATA=F.readlines()
F.close()
for x in range(len(DATA)) :
    a = DATA[x]
    b = a.split(',')
    DATA[x] = b
    print DATA[x]
for i in xrange(len(DATA)):
    for j in xrange(len(DATA[i])):
        DATA[i][j] = float(DATA[i][j])
print DATA[0]
#X_train=numpy.array(DATA)
#Sprint "X_train\n",X_train

#mpl.scatter(X_train[:, 0], X_train[:, 1], c='white')
#mpl.show()