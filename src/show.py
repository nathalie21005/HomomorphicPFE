''' this script shows the original and the PCA reconstructed 
images, you just have to supply a faceEuclideanDistance number from the data set 
see help-show-py.txt for more details''' 

from mean_face import mean_face
#from eigenfaces import eigenfaces  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm # color map 
import pylab


#print mean_face

#E=eigenfaces.split('\n')
#M = np.matrix([[float(x) for x in e.split()] for e in E])
#np.save("eigenfaces",M)

M=np.load("eigenfaces.npy")

print "give me a faceEuclideanDistance number..." 
print "from training dataset (1223-->3222)"
#print "testing (3223-->5222)"
nb = raw_input()
#nb="1223"

with open ("../faces/faceR") as faceR:
    w=[]
    for v in faceR:
        if v.split()[0]!=nb:
            pass
        else:
            w=[float(x) for x in v.split()[1:]]
            break  
    
    
    if v.split()[0] == nb:  
        print "PCA reconstructed ..."
        f = plt.figure()
        f.add_subplot(121)
        i = M.transpose().dot(w) +     mean_face.transpose()
        plt.imshow(i.reshape(128,128), cmap = cm.Greys_r)  # @UndefinedVariable
        #pylab.show()
        
        print "original ..."
        f.add_subplot(122)
        orig = np.fromfile("../faces/rawdata/rawdata/"+nb, dtype=np.uint8)        
        #print len(orig)
        #print 128*128  
        plt.imshow(orig.reshape(128,128), cmap = cm.Greys_r)
        pylab.show() 