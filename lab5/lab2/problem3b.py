##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 2                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.3a                                 #
##############################################

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages') 
from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer, SigmoidLayer, LinearLayer, TanhLayer
import pickle
import cv2

def loadImage(path):
    im = cv2.imread(path)
    return flatten(im)
 
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def detect(value):
    if (-5)<value<=5:
        animal='giraffe'
    elif 5<value<=15:
        animal='dog'
    elif 15<value<=25:
        animal='gorilla'
    elif 25<value<=35:
        animal='alligator'
    elif 35<value<=45:
        animal='cat'
    else:
        animal='cannot detect'
    return animal

if __name__ == "__main__":
 
    t = loadImage('pic/giraffe1.png')
    #net = buildNetwork(len(t),.02*len(t), .02*len(t), 1)
    #net = buildNetwork(len(t), .03*len(t),.03*len(t),.03*len(t),1, hiddenclass=SoftmaxLayer, bias = True)
    net = buildNetwork(len(t), .03*len(t),.03*len(t),1)
    #net = buildNetwork(len(t), .03*len(t), 1)
    #net = buildNetwork(len(t), .03*len(t), 1, hiddenclass=TanhLayer, bias = True)
    #net = buildNetwork(2, 4, 1, bias=True)
    ds = SupervisedDataSet(len(t), 1)
    ds.addSample(loadImage('pic/giraffe1.png'),(0,))
    ds.addSample(loadImage('pic/giraffe2.png'),(0,))
    ds.addSample(loadImage('pic/giraffe3.png'),(0,))
    ds.addSample(loadImage('pic/giraffe4.png'),(0,))
    ds.addSample(loadImage('pic/giraffe5.png'),(0,))
    #ds.addSample(loadImage('pic/giraffe6.png'),(0,))
    ds.addSample(loadImage('pic/dog1.png'),(10,))
    ds.addSample(loadImage('pic/dog2.png'),(10,))
    ds.addSample(loadImage('pic/dog3.png'),(10,))
    ds.addSample(loadImage('pic/dog4.png'),(10,))
    ds.addSample(loadImage('pic/dog5.png'),(10,))
    #ds.addSample(loadImage('pic/dog6.png'),(10,))
    ds.addSample(loadImage('pic/gorilla1.png'),(20,))
    ds.addSample(loadImage('pic/gorilla2.png'),(20,))
    ds.addSample(loadImage('pic/gorilla3.png'),(20,))
    ds.addSample(loadImage('pic/gorilla4.png'),(20,))
    ds.addSample(loadImage('pic/gorilla5.png'),(20,))
    #ds.addSample(loadImage('pic/gorilla6.png'),(20,))
    ds.addSample(loadImage('pic/alligator1.png'),(30,))
    ds.addSample(loadImage('pic/alligator2.png'),(30,))
    ds.addSample(loadImage('pic/alligator3.png'),(30,))
    ds.addSample(loadImage('pic/alligator4.png'),(30,))
    ds.addSample(loadImage('pic/alligator5.png'),(30,))
    #ds.addSample(loadImage('pic/alligator6.png'),(30,))
    ds.addSample(loadImage('pic/cat1.png'),(40,))
    ds.addSample(loadImage('pic/cat2.png'),(40,))
    ds.addSample(loadImage('pic/cat3.png'),(40,))
    ds.addSample(loadImage('pic/cat4.png'),(40,))
    ds.addSample(loadImage('pic/cat5.png'),(40,))
    #ds.addSample(loadImage('pic/cat6.png'),(40,))
    trainer = BackpropTrainer(net, ds)
    error = 10
    iteration = 0
    while error > 0.0001: 
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
 

    #printing
    test=['pic/giraffe6.png',
          'pic/dog6.png',
          'pic/gorilla6.png',
          'pic/alligator6.png',
          'pic/cat6.png'
           ] 
    print '\n\n===RESULT===='
    for pict in test:
        value=net.activate(loadImage(pict))
        animalname=detect(value)
        print "Picture %s has a %s  | with the value= %f" % (pict, animalname,value)
        #print "[DEBUG] value of %s is %f" % (pict,value)
