##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 2                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.2b                                 #
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
 
if __name__ == "__main__":
 
    t = loadImage('pic/drp1.png')
    #net = buildNetwork(len(t),.02*len(t), .02*len(t), 1)
    net = buildNetwork(len(t), .03*len(t),.03*len(t),.03*len(t), 1)
    #net = buildNetwork(len(t), .03*len(t), 1, hiddenclass=TanhLayer, bias = True)
    #net = buildNetwork(2, 4, 1, bias=True)
    ds = SupervisedDataSet(len(t), 1)
    ds.addSample(loadImage('pic/drp1.png'),(1,))
    ds.addSample(loadImage('pic/drp2.png'),(1,))
    ds.addSample(loadImage('pic/drp3.png'),(1,))
    ds.addSample(loadImage('pic/drp4.png'),(1,))
    ds.addSample(loadImage('pic/drp5.png'),(1,))
    ds.addSample(loadImage('pic/drp6.png'),(1,))
    ds.addSample(loadImage('pic/drp7.png'),(1,))
    ds.addSample(loadImage('pic/drp8.png'),(1,))
    ds.addSample(loadImage('pic/other1.png'),(15,))
    ds.addSample(loadImage('pic/other2.png'),(15,))
    ds.addSample(loadImage('pic/other3.png'),(15,))
    ds.addSample(loadImage('pic/other4.png'),(15,))
    ds.addSample(loadImage('pic/other5.png'),(15,))
    ds.addSample(loadImage('pic/other6.png'),(15,))
    ds.addSample(loadImage('pic/other7.png'),(15,))
    ds.addSample(loadImage('pic/other8.png'),(15,))
    #trainer = BackpropTrainer(net, ds, learningrate = 0.1, momentum = 0.99)
    #trainer = BackpropTrainer(net, ds, learningrate = 0.5, momentum = 0.5)
    trainer = BackpropTrainer(net, ds)
    error = 10
    iteration = 0
    while error > 0.0001: 
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
 
    print "\nResult: ", net.activate(loadImage('pic/group1.png'))
    print "\nResult: ", net.activate(loadImage('pic/group2.png'))
    print "\nResult: ", net.activate(loadImage('pic/drp9.png'))
    print "\nResult: ", net.activate(loadImage('pic/drp10.png'))
