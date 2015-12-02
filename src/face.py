import os
import math
from math import *
from lib2to3.fixer_util import String
from _ast import List
print os.getcwd()

def euclidean_distance(x,y): #function of distance but i don't use it
    return sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))

my_listS = list()
my_listR = list()

with open('D:\\ProjectPFE\\faces\\faceS', 'r') as f:
    lineS= f.readlines()
    class MagicString(str):
            magicSplit = str.split
with open('D:\\ProjectPFE\\faces\\faceR', 'r') as fr:
    lineR= fr.readlines()
    for y in range (len(lineR)):
        lineRaray =MagicString(lineR[y]).magicSplit()#list of images in array ['','','',...]
        my_listR.append(lineRaray)#its all images of faceR
#        print(lineRaray) #first line of faceR without number of image
    for x in range(len(lineS)):
        LineSAray=MagicString(lineS[x]).magicSplit()#list of images in array ['','','',...]
#        print LineSAray[1]
        my_listS.append(LineSAray)#its all images of faceS
        #        print(LineSAray) #first line of faceS without number of image 
jss=0
iss=0
a=0
list_distance= list()
for iss in range(len(my_listS)): 
#    print my_listS[iss] #first line of faceS 3223
    for irr in range(len(my_listR)): 
#        print my_listR[irr] #first line of faceR 1223
        for jss in range (len(my_listS[iss])): 
            for jrr in range (len(my_listR[irr])):
                jss=jss+1
                if jss<len(my_listS[iss]):
                    x= my_listS[iss][jss] #each value from image from faceS
                    y =my_listR[irr][jrr] #each value from image from faceR
                    print x, y # only coefficient of two images
                    zz=pow((float(x))-(float(y)),2)
#                    print zz 
                    a=a+zz# sum of distance each image
#                print a
            list_distance.append(math.sqrt(a)) #distance euclidean final of image 3223 with faceR
            print list_distance
    irr=irr+1

