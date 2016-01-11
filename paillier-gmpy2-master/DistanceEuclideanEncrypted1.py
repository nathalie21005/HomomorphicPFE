import os
from paillier_gmpy2 import *
import sys 
import random
import time 
print os.getcwd()

#define k 
k = 15

listdist=list()
list_v_2=list()
decryptV_2=list()
list_w_2=list()
list_dw_2=list()
list_2_y=list()
listdistance=list()

print "choose from testing dataset (3223-->5222)"
nb = input()

v=[]
with open ("../faces/faceS") as faceS:
    found = False 
    for line in faceS:
        if not line.startswith(" %d " % nb ):
            pass
        else:
            v = [ float (x) for x in line.split()[1:] ]
            found = True 
            break  
    if not found:
        print "face not found!"
        sys.exit()

with open('../faces/faceR', 'r') as fR:
        lines= fR.readlines()
        faceR = {}
        distTo = {}
        for line in lines:
            w = line.split()
            faceR [int(w[0])]= [float (y) for y in w[1:] ]
            #print faceR [int(w[0])]
            
            
#function of encrypted distance 
def encrypt_euclidean_distance(v,w):
    print "v = ", v
    xn=[int(float(x)*(10**6)) for x in v]
    cv=[encrypt(pub,int(cxx)) for cxx in xn]
    for x in v:
        v_2=int(float(x)*(10**6))*int(float(x)*(10**6))
        Vv_2=v_2*(10**-12)
        list_v_2.append(Vv_2)
    print "v_2 =", list_v_2
    v_2=[int(float(x)*(10**6))*int(float(x)*(10**6)) for x in v]
    cv_2=[encrypt(pub,int(xx_2)) for xx_2 in v_2]
    for cxx_2 in cv_2:
        dv_2= decrypt(priv, pub, cxx_2) 
        dv_2=dv_2*(10**-12)
        decryptV_2.append(dv_2)
    print "dv_2 =", decryptV_2
    
    
    print "w = ", w
    for y in w:
        w_2=int(float(y)*(10**6))*int(float(y)*(10**6)) 
        w_2=w_2*(10**-12)
        list_w_2.append(w_2)
    print "w_2 = ", list_w_2
    w_2=[int(float(y)*(10**6))*int(float(y)*(10**6)) for y in w]
    cw_2=[encrypt(pub,int(yy_2)) for yy_2 in w_2]
    for cyy_2 in cw_2:
        dw_2=decrypt(priv, pub, cyy_2) 
        dw_2=dw_2*(10**-12)
        list_dw_2.append(dw_2)
    print "dw_2 =", list_dw_2
    

    add= [e_add(pub, cx_2, cy_2 ) for (cx_2),(cy_2) in zip(cv_2, cw_2)]
    #print "add =",add
 
    w2=[(-2)*float(y) for y in w]
    #print "w2", w2
    for zz in w2:
        if zz < 0:
            multiplication =zz % pub.n
            list_2_y.append(multiplication)
        else:
            multiplication= zz
            list_2_y.append(multiplication)
    print "-2*Y",list_2_y
    multi= [e_mul_const(pub, cx, int(float(y)*(10**6))) for (cx),(y) in zip(cv, list_2_y)] # w2=2*w=[2*y1, 2*y2, .. , 2*y99]
    print "multiiiii",multi
       
 
    dist=[e_add(pub, a, b) for a, b in zip(add, multi)]    
    return dist


print "Generating keypair... %d bits" % 512
priv, pub = generate_keypair(512)

for f in faceR.keys(): 
    distTo[f]=encrypt_euclidean_distance(v,faceR[f])
    print "encrypted distance = ", distTo[f]
    for c in distTo[f]:
        zz=decrypt(priv, pub, c) 
        if zz > pub.n/2 :
            listdistance.append(zz - pub.n)
        else:
            listdistance.append(zz)
      
#print "Decryption of distance =", listdistance