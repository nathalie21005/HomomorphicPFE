import os
import sys 
import math
import re
#define k 
k = 4
Accuracy_gender, Accuracy_age, Accuracy_race,Accuracy_impression= 0,0,0,0
#function of distance but I use it!
def euclidean_distance(x,y): 
    return math.sqrt(sum(pow((a)-(b),2) for (a), (b) in zip(x,y)))

with open('../faces/faceS', 'r') as f:
    #lineS= f.readlines()
    for lineS in f:
        imgTes =[ float (x) for x in lineS.split()[0:] ]
        imgTest = [ float (y) for y in lineS.split()[1:] ]
        print  int(imgTes[0]), imgTest
        with open('../faces/faceR', 'r') as faceR:
            lines= faceR.readlines()
            faceR = {}
            distTo = {}
            for line in lines:
                v = line.split()
                faceR [int(v[0])]= [float(x) for x in v[1:] ]
        
            for f in faceR.keys(): 
                distTo[f]=euclidean_distance(imgTest,faceR[f])
        
            distances = [ (x, distTo[x] )for x in distTo.keys()]
            distances.sort(key=lambda x: x[1])
            distances = distances [:k]
            print distances
        # check the labels
        wlabels = {}
        with open ("../faces/faceDS") as faceDS:
        
            found = False 
            for line in faceDS:
                if not line.startswith(" %d " % int(imgTes[0]) ):
                    pass
                else:
                    tokens  = re.split(r'[( )]',line)
                    if len(tokens)>20:
                        wlabels["gender"]= tokens[5]
                        wlabels["age"]= tokens[10]
                        wlabels["race"]= tokens[14]
                        wlabels["impression"]= tokens[18]
                        #print wlabels
                        found = True 
                    break  
            if not found:
                print "face not found!"
                #sys.exit()
        with open('../faces/faceDR', 'r') as faceDR:
            distances.sort(key = lambda x: x[0])
            print distances 
            Cgender, Cage, Crace, Cimpression =0, 0, 0, 0 
            i=0
            print int(imgTes[0]), wlabels.values() 
            print "nei |gender | age | race | impression "
            for line in faceDR:
                #print line
                if line.startswith(" %d " % distances[i][0]):
                    
                    tokens = re.split(r'[( )]',line)
                     
                    #print len(tokens)
                    if len(tokens)>20:
                        print distances[i][0], tokens[5], tokens[10], tokens[14], tokens[18]
                        if tokens[5] == wlabels["gender"]: 
                            Cgender+=1
                        if tokens[10] == wlabels["age"]:
                            Cage+=1
                        if tokens[14] == wlabels["race"]:
                            Crace+=1
                        if tokens[18] == wlabels["impression"]:
                            Cimpression+=1
                        i+=1
                        if i==k: 
                            break 
        
            print Cgender, Cage, Crace, Cimpression
            print Cgender>k/2, Cage>k/2, Crace>k/2, Cimpression>k/2
            if Cgender>k/2 :
                Accuracy_gender+=1
            if Cage>k/2 :
                Accuracy_age+=1
            if Crace>k/2 :
                Accuracy_race+=1
            if Cimpression>k/2 :
                Accuracy_impression+=1
            print Accuracy_gender, Accuracy_age, Accuracy_race,Accuracy_impression