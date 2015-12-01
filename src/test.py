import os
from math import *
from lib2to3.fixer_util import String
from _ast import List
print os.getcwd()
def euclidean_distance(x,y):
    return sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))
#print euclidean_distance([xx],[yy])
my_listS = list()
my_listR = list()
with open('D:\\ProjectPFE\\faces\\faceS', 'r') as f:
    lineS= f.readlines()
    lineSWithoutNumber=lineS[0]
    class MagicString(str):
            magicSplit = str.split
with open('D:\\ProjectPFE\\faces\\faceR', 'r') as fr:
    lineR= fr.readlines()
    #lineRWithoutNumber= lineR[0]
    for y in range (len(lineR)):
        lineRaray =MagicString(lineR[y]).magicSplit()#list of images in array ['','','',...]
        my_listR.append(lineRaray)#its all images of faceR
#        print(lineRaray) #first line of faceR without number of image
    for x in range(len(lineS)):
        LineSAray=MagicString(lineS[x]).magicSplit()#list of images in array ['','','',...]
        my_listS.append(LineSAray)#its all images of faceS
        #        print(LineSAray) #first line of faceS without number of image 
for yr in range (len(lineRaray)-5):
    yy =lineRaray[yr+5]
#    my_list.append(lineRaray[yr])
#    print my_list
#    print euclidean_distance([yy.values()],[67.9])
#   print(lineRaray[yr+5])#all lines of faceR
for xs in range (len(LineSAray)-5):
    xx=LineSAray[xs+5]
#    print(LineSAray[xs+5])#all lines of faceS
#only last lines of images R
#print my_listS
#c='1880.258789'
#[(i, my_listR.index(c))
# for i, my_listR in enumerate(my_listR)
# if c in my_listR]
#print my_listR
#only last lines of images S
#c='1509.810059'
#[(i, my_listS.index(c))
#for i, my_listS in enumerate(my_listS)
#if c in my_listS]
for i in range(len(my_listS)): 
#    print my_listS[i] #each image from all images of faceS
    for j in range (len(my_listS[i])): 
        x= my_listS[i][j] #each value from image from faceS
for i in range(len(my_listR)): 
#    print my_listR[i] #each image from all images of faceR
    for j in range (len(my_listR[i])): 
        y =my_listR[i][j] #each value from image from faceR  
        print euclidean_distance([float(my_listS[i][j])],[float(my_listR[i][j])])
                