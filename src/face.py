import os
import math
from math import *
from lib2to3.fixer_util import String
from _ast import List
print os.getcwd()

def euclidean_distance(x,y): #function of distance but i don't use it
    return sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))
def quickSort(lst):
    if len(lst) <= 1: 
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(smaller) + [lst[0]] + quickSort(larger)
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
<<<<<<< HEAD
        print my_listR
=======
#        print(lineRaray) #first line of faceR without number of image
    for x in range(len(lineS)):
        LineSAray=MagicString(lineS[x]).magicSplit()#list of images in array ['','','',...]
#        print LineSAray[1]
        my_listS.append(LineSAray)#its all images of faceS
        #        print(LineSAray) #first line of faceS without number of image 
nassar = 1 
jrr=0
jss=0
iss=0
a=0
list_distance= list()
for iss in range(len(my_listS)): 
#    print my_listS[iss] #first line of faceS 3223
    for irr in range(2000): 
#        print my_listR[irr] #first line of faceR 1223
        a=0 
        for jss in range (100): 
            jss=0
            for jrr in range (100):
#                jrr=jrr+1
                if jrr<99:
                    x= my_listS[iss][jss+1] #each value from image from faceS
                    y =my_listR[irr][jrr+1] #each value from image from faceR
                    #print x, y # only coefficient of two images
                    zz=pow((float(x))-(float(y)),2)
    #                    print zz 
                    a=a+zz# sum of distance each image
                    jrr=jrr+1
                    jss=jss+1
                    #print jss, jrr
                else:# and jss>=99:
                   # print 'jrr'
                    irr=irr+1
                    
                    print iss, irr
                    if irr>=2000:
                        print list_distance
                        #print list_distance.sort()
                    jrr=0 
        print a
        q=math.sqrt(a)#distance of each line
        list_distance.append(q) #still to modified for put an array
        print list_distance
        


>>>>>>> origin/master
