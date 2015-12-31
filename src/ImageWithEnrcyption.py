import os
from paillier_gmpy2 import *
import sys 
import random
import time 
print os.getcwd()
coefficient_encrypted=list()
print "give me a faceEuclideanDistance number..." 
print "from training dataset (3223-->5222)"
#print "testing (3223-->5222)"
nb = raw_input()
#nb="1223"

with open ("../faces/faceS") as faceR:
    w=[]
    for v in faceR:
        if v.split()[0]!=nb:
            pass
        else:
            w=[u for u in v.split()[1:]]
            break  
    if v.split()[0] == nb:
        iss=int(nb)-3222 
print "Generating keypair... %d bits" % 512
priv, pub = generate_keypair(512)
for iss in range(0,99):
    x= w[iss] #99 coefficients of each image in FaceS 
    print "x =", x
    xx = float(x) *(10**6)
    
    #print "Encrypting x..."
    encryptx = encrypt(pub, int(xx))
    print "cx =", encryptx
    
    print "Decrypting cx..."
    z = decrypt(priv, pub, encryptx)
    
    if z > pub.n/2 :
        print "dx=", round(z-pub.n)*(10**-6)
    else:
        print "dx=", round(z)*(10**-6)
    coefficient_encrypted.append(encryptx)
print coefficient_encrypted