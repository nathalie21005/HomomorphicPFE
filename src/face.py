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