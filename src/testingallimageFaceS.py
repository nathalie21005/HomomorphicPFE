import os
import math
import re
from math import *
from lib2to3.fixer_util import String
from _ast import List
print os.getcwd()
c_gen, c_ag, c_ra, c_imp =0, 0, 0, 0 
jrr=0
jss=0

jrr=0
a=0
val=1224
list_distance= list()
list_dist_for_sort=list()
List_imagenumber_distance=list()
list_with_sort=list()
list_min_5dist=list()
my_listDR=list()
my_listR=list()
my_list_nbreofimage=list()
def euclidean_distance(x,y):
    return sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))
#print euclidean_distance([xx],[yy])
my_listS = list()
my_listR = list()
def quickSort(lst):
    if len(lst) <= 1: 
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(smaller) + [lst[0]] + quickSort(larger)

with open('../faces/faceS', 'r') as f:
    lineS= f.readlines()
    lineSWithoutNumber=lineS[0]
    class MagicString(str):
            magicSplit = str.split
with open('../faces/faceR', 'r') as fr:
    lineR= fr.readlines()
    for y in range (len(lineR)):
            lineRaray =MagicString(lineR[y]).magicSplit()#list of images in array ['','','',...]
            my_listR.append(lineRaray)#its all images of faceR
            #print my_listR
    #lineRWithoutNumber= lineR[0]
    for x in range(len(lineS)):
        LineSAray=MagicString(lineS[x]).magicSplit()#list of images in array ['','','',...]
        my_listS.append(LineSAray)#its all images of faceS
        #print LineSAray #first line of faceS without number of image 
        nb=LineSAray[0]
        
        for iss in range(0,1):
            iss=0
            print nb
            my_list_nbreofimage=list()
            List_imagenumber_distance=list()
            for irr in range(len(my_listR)): 
        #        print my_listR[irr] #first line of faceR 1223
                a=0 
                list_distance= list()
                for jss in range (1,100): 
                    jss=0
                    for jrr in range (1,100):
                        x= LineSAray[jss] #each value from image from faceS
                       # print x
                        y =my_listR[irr][jrr] #each value from image from faceR
                        #print x,y
                        zz=pow((float(x))-(float(y)),2)
                        a=a+zz# sum of distance each image
                        jss=jss+1                                        
                q=math.sqrt(a)#distance of each line
                list_distance.append(irr) #still to modified for put an array
                list_distance.append(q)
                #print list_distance
                List_imagenumber_distance.append(list_distance)
            print List_imagenumber_distance
            for indice_in_List_imagenumber_distance in range (len(List_imagenumber_distance)):
                x=List_imagenumber_distance[indice_in_List_imagenumber_distance][1]
                list_dist_for_sort.append(x)
            list_with_sort=quickSort(list_dist_for_sort)
            print list_with_sort
            for indice in range(0,5):
                for indice_in_List_imagenumber_distance in range (len(List_imagenumber_distance)):
                    if list_with_sort[indice]== List_imagenumber_distance[indice_in_List_imagenumber_distance][1]:
                        my_list_nbreofimage.append(List_imagenumber_distance[indice_in_List_imagenumber_distance][0]+val) #number of image
            print my_list_nbreofimage
            
            with open ("C:\\Users\\Acer\\Desktop\\faces\\faceDS") as faceDS:
                for v in faceDS:
                    if v.split()[0] == nb:
                        lineSRaray =re.split(r'[( )]',v)
                        #print lineSRaray
                        gender = lineSRaray[5]
                        age= lineSRaray[10]
                        race=lineSRaray[14]
                        impression=lineSRaray[18]
                print gender, age, race, impression 
            with open('C:\\Users\\Acer\\Desktop\\faces\\faceDR', 'r') as f:
                lineDR= f.readlines()
                gen, ag, ra, imp =0, 0, 0, 0 
                for index in range(len(lineDR)):
                    lineDRaray =re.split(r'[( )]',lineDR[index])
                    #print lineDRaray[1], my_list_nbreofimage[0]
                    for x in my_list_nbreofimage :
                        if lineDRaray[1] == str(x) or lineDRaray[1]== str(x) or lineDRaray[1]==str(x) or lineDRaray[1]== str(x) or lineDRaray[1]== str(x):
                            print lineDRaray# 5 list 
                            if lineDRaray[5] == gender: 
                                gen+=1
                            if lineDRaray[10]==age: 
                                ag+=1
                            if lineDRaray[14]==race : 
                                ra+=1
                            if lineDRaray[18]== impression: 
                                imp+=1
                            print  gen,ag, ra, imp 
            if gen >=3 : 
                c_gen+=1
            if ag >=3:
                c_ag+=1
            if ra>=3 :
                c_ra+=1
            if imp>=3 :
                c_imp+=1 
            print lineDRaray[3], ":" ,gender , c_gen,lineDRaray[8],":", age,c_ag,lineDRaray[13],":", race,c_ra,lineDRaray[17],":", impression,c_imp
   
