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



class MagicString(str):
            magicSplit = str.split
jrr=0
jss=0
iss=0
jrr=0
a=0
val=1224
list_distance= list()
list_dist_for_sort=list()
List_imagenumber_distance=list()
list_with_sort=list()
list_min_5dist=list()
my_listDR=list()
my_list_nbreofimage=list()
##    print my_listS[iss] #first line of faceS 3223
my_listFaceS=list()
with open('D:\\ProjectPFE\\faces\\faceS', 'r') as fr:
    lineS= fr.readlines()
    for y in range (len(lineS)):
        lineSaray =MagicString(lineS[y]).magicSplit()#list of images in array ['','','',...]
        my_listFaceS.append(lineSaray)
    #print my_listFaceS # list of list contain all images of FaceS
for iss in range(len(my_listFaceS)):
    for irr in range(len(my_listFaceR)): 
#        print my_listR[irr] #first line of faceR 1223
        a=0 
        list_distance= list()
        for jss in range (1,100): 
            jss=0
            for jrr in range (1,100):
    #                jrr=jrr+1
                #if jrr<99:
                x= my_listFaceS[0][jss] #each value from image from faceS
                y =my_listFaceR[irr][jrr] #each value from image from faceR
                zz=pow((float(x))-(float(y)),2)
                a=a+zz# sum of distance each image
                jss=jss+1                                        
        q=math.sqrt(a)#distance of each line
        list_distance.append(irr) #still to modified for put an array
        list_distance.append(q)
        #print quickSort(list_distance)
        List_imagenumber_distance.append(list_distance)
    print List_imagenumber_distance
for indice_in_List_imagenumber_distance in range (len(List_imagenumber_distance)):
    x=List_imagenumber_distance[indice_in_List_imagenumber_distance][1]
    list_dist_for_sort.append(x)
list_with_sort=quickSort(list_dist_for_sort)
print list_with_sort
for indice in range(0,5):
    #print list_with_sort[indice]# 5 plus petit distance
    for indice_in_List_imagenumber_distance in range (len(List_imagenumber_distance)):
        if list_with_sort[indice]== List_imagenumber_distance[indice_in_List_imagenumber_distance][1]:
            my_list_nbreofimage.append(List_imagenumber_distance[indice_in_List_imagenumber_distance][0]+val) #number of image
print my_list_nbreofimage