''' this code takes one face number as input 
and computes the euclidean distance to all the training 
faces, then it returns the k nearest ones''' 

import os
import sys 
import math
import re

#define k 
k = 15

#function of distance but I use it!
def euclidean_distance(x,y): 
    return math.sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))
    
print "choose from testing dataset (3223-->5222)"
#nb = input()
nb = 4100 

#check up the face 
w=[]
with open ("../faces/faceS") as faceS:
    found = False 
    for line in faceS:
        if not line.startswith(" %d " % nb ):
            pass
        else:
            w = [ float (x) for x in line.split()[1:] ]
            found = True 
            break  
    if not found:
        print "face not found!"
        sys.exit()
#print w 

# compute k nearest neighbors 
with open('../faces/faceR', 'r') as faceR:
    lines= faceR.readlines()
    faceR = {}
    distTo = {}
    for line in lines:
        v = line.split()
        faceR [int(v[0])]= [float(x) for x in v[1:] ]

    for f in faceR.keys(): 
        distTo[f]=euclidean_distance(w,faceR[f])

    distances = [ (x, distTo[x] )for x in distTo.keys()]
    distances.sort(key=lambda x: x[1])
    distances = distances [:k]
    #print distances 

# check the labels
wlabels = {}
with open ("../faces/faceDS") as faceDS:

    found = False 
    for line in faceDS:
        if not line.startswith(" %d " % nb ):
            pass
        else:
            tokens  = re.split(r'[( )]',line)
             
            wlabels["gender"]= tokens[5]
            wlabels["age"]= tokens[10]
            wlabels["race"]= tokens[14]
            wlabels["impression"]= tokens[18]
            #print wlabels
            found = True 
            break  
    if not found:
        print "face not found!"
        sys.exit()

with open('../faces/faceDR', 'r') as faceDR:
    distances.sort(key = lambda x: x[0])
    print distances 
    Lgender, Lage, Lrace, Limpression = [], [], [], [] 
    i=0
    print nb, wlabels.values() 
    print "nei |gender | age | race | impression "
    for line in faceDR:
        #print line
        if line.startswith(" %d " % distances[i][0]):
            
            tokens = re.split(r'[( )]',line)
            print distances[i][0], tokens[5], tokens[10], tokens[14], tokens[18] 
            #if tokens[5] == wlabels["gender"]: 
            Lgender.append(tokens[5])

            #if tokens[10] == wlabels["age"]:
            Lage.append(tokens[10])
            #if tokens[14] == wlabels["race"]:
            Lrace.append(tokens[14])
            #if tokens[18] == wlabels["impression"]:
            Limpression.append(tokens[18])
            i+=1
            if i==k: 
                break 

    from collections import Counter
    Cgender = Counter( Lgender) 
    Cage = Counter (Lage) 
    Crace = Counter (Lrace) 
    Cimpression = Counter (Limpression) 
    print wlabels["gender"] ==  Cgender.most_common()[0][0] ,\
     wlabels["age"] == Cage.most_common()[0][0] ,\
     wlabels["race"] == Crace.most_common()[0][0], \
     wlabels["impression"] == Cimpression.most_common()[0][0]

