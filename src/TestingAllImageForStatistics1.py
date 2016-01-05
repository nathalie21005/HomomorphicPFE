import os
import sys 
import math
import re
from time import time 

from faceEuclideanDistance1 import classify, euclidean_distance 

#define k 
k = 15
nb_gender, nb_age, nb_race, nb_impression = 0, 0, 0, 0 
total=0
# we want to classify each face in the faceS (testing dataset)
t0 = time()
with open ("../faces/faceS") as faceS, open ("../faces/faceDS") as faceDS:
    for line, wline  in zip(faceS, faceDS):
        
        coef = line.split()
        nb = coef[0]
        #print nb 
        w = [ float (x) for x in coef[1:] ]
        wlabels = {}
        try: 
            tokens  = re.split(r'[( )]',wline)
            wlabels["gender"]= tokens[5]
            wlabels["age"]= tokens[10]
            wlabels["race"]= tokens[14]
            wlabels["impression"]= tokens[18]

        except: 
            print line 
            print wline 
            print wlabels 
            print sys.exc_info()[0]
            continue  
        # I want to see if error comes from classification 
        # (i.e. from the training data set )   
        try: 
            res = classify (w, wlabels, k)
            total+=1
            if res[0]: 
                nb_gender+=1
            if res[1]: 
                nb_age+=1
            if res[2]: 
                nb_race+=1
            if res[3]: 
                nb_impression+=1
            print "--", total
        except: 
            print "classification error" 
            print sys.exc_info()[0]
            break 

       

print "classification time:", round(time()-t0, 3), "s"
print k 
print total 
print nb_gender, nb_age, nb_race, nb_impression 
print nb_gender*1.0/total, nb_age*1.0/total, nb_race*1.0/total, nb_impression*1.0/total 