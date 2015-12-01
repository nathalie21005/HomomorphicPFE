import os
import math
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
        my_listSS=my_listS[0]
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
jss=2
jrr=2
a=0
iss=1
list_distance= list()
if iss<len(my_listSS)-1:
    for iss in range(len(my_listSS)): 
        print my_listSS[iss+1]
        for irr in range(len(my_listR)): 
            if jss<99 and jrr<99 :
                for jss in range (len(my_listSS[iss+1])): 
                    for jrr in range (len(my_listR[irr+1])):
                        x= my_listSS[iss+1][1] #each value from image from faceS
                        y =my_listR[irr+1][1] #each value from image from faceR
#                    print x, y
                    jss=jss+1
                    zz=pow((float(x))-(float(y)),2) 
                jrr=jrr+1
                a=a+zz# sum of distance 
#                print math.sqrt(a) #distance euclidean final of image 3223 1223
    irr=irr+1
    iss=iss+1
#        print a
#        distance= math.sqrt(99)
#list_distance.append(euclidean_distance([float(x)],[float(y)]))
#print math.sqrt(100)
