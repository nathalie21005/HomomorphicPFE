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
        print my_listR
    for x in range(len(lineS)):
        LineSAray=MagicString(lineS[x]).magicSplit()#list of images in array ['','','',...]
#        print LineSAray[1]
        my_listS.append(LineSAray)#its all images of faceS
        #        print(LineSAray) #first line of faceS without number of image 
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
for irr in range(len(my_listR)): 
#        print my_listR[irr] #first line of faceR 1223
    a=0 
    list_distance= list()
    for jss in range (1,100): 
        jss=0
        for jrr in range (1,100):
#                jrr=jrr+1
            #if jrr<99:
            x= my_listS[0][jss] #each value from image from faceS
            y =my_listR[irr][jrr] #each value from image from faceR
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
for indice in range(0,5):
    #print list_with_sort[indice]# 5 plus petit distance
    for indice_in_List_imagenumber_distance in range (len(List_imagenumber_distance)):
        if list_with_sort[indice]== List_imagenumber_distance[indice_in_List_imagenumber_distance][1]:
            my_list_nbreofimage.append(List_imagenumber_distance[indice_in_List_imagenumber_distance][0]+val) #number of image
print my_list_nbreofimage
with open('D:\\ProjectPFE\\faces\\faceDR', 'r') as f:
    lineDR= f.readlines()
    for dr in range (len(lineDR)):
        lineRaray =MagicString(lineDR[dr]).magicSplit()#list of images in array ['','','',...]
        my_listDR.append(lineRaray)
        #print my_listDR
#for indice_number_image in range(len(my_list_nbreofimage)):
for indice_DR in range(len(my_listDR)):
    for indice_DR_line in range(len(my_listDR[indice_DR])):
        #print my_list_nbreofimage[indice_number_image]
        print my_listDR[indice_DR][indice_DR_line]
        for indice_number_image in range(len(my_list_nbreofimage)):
            if my_listDR[indice_DR][indice_DR_line]==2254:
                print'testing'
                print my_listDR[indice_DR][indice_DR_line]
    indice_DR=indice_DR+1