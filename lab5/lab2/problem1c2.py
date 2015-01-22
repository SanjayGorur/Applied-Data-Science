##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 2                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1c                                 #
##############################################

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def problemA():
    ds_and = SupervisedDataSet(3, 1)
    ds_and = SupervisedDataSet(3, 1)
    ds_and.addSample( (0,0,0) , (0,))
    ds_and.addSample( (0,0,1) , (1,))
    ds_and.addSample( (0,1,0) , (0,))
    ds_and.addSample( (0,1,1) , (1,))
    ds_and.addSample( (1,0,0) , (0,))
    ds_and.addSample( (1,0,1) , (1,))
    ds_and.addSample( (1,1,0) , (1,))
    ds_and.addSample( (1,1,1) , (1,))
    net = buildNetwork(3, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_and, 3000)
    trainer.testOnData() 
    print '\n1)  (A AND B) OR C :'
    print '0 0 0  = ', net.activate((0,0,0))
    print '0 0 1  = ', net.activate((0,0,1))
    print '0 1 0  = ', net.activate((0,1,0))
    print '0 1 1  = ', net.activate((0,1,1))
    print '1 0 0  = ', net.activate((1,0,0))
    print '1 0 1  = ', net.activate((1,0,1))
    print '1 1 0  = ', net.activate((1,1,0))
    print '1 1 1  = ', net.activate((1,1,1))

def problemB():
    ds_and = SupervisedDataSet(3, 1)
    ds_and = SupervisedDataSet(3, 1)
    ds_and.addSample( (0,0,0) , (0,))
    ds_and.addSample( (0,0,1) , (1,))
    ds_and.addSample( (0,1,0) , (0,))
    ds_and.addSample( (0,1,1) , (0,))
    ds_and.addSample( (1,0,0) , (0,))
    ds_and.addSample( (1,0,1) , (0,))
    ds_and.addSample( (1,1,0) , (0,))
    ds_and.addSample( (1,1,1) , (1,))
    net = buildNetwork(3, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_and, 3000)
    trainer.testOnData() 
    print '\n2)(NOT (A OR B)) AND C'
    print '0 0 0  = ', net.activate((0,0,0))
    print '0 0 1  = ', net.activate((0,0,1))
    print '0 1 0  = ', net.activate((0,1,0))
    print '0 1 1  = ', net.activate((0,1,1))
    print '1 0 0  = ', net.activate((1,0,0))
    print '1 0 1  = ', net.activate((1,0,1))
    print '1 1 0  = ', net.activate((1,1,0))
    print '1 1 1  = ', net.activate((1,1,1))

def problemC():
    ds_and = SupervisedDataSet(3, 1)
    ds_and = SupervisedDataSet(3, 1)
    ds_and.addSample( (0,0,0) , (1,))
    ds_and.addSample( (0,0,1) , (1,))
    ds_and.addSample( (0,1,0) , (1,))
    ds_and.addSample( (0,1,1) , (0,))
    ds_and.addSample( (1,0,0) , (1,))
    ds_and.addSample( (1,0,1) , (0,))
    ds_and.addSample( (1,1,0) , (1,))
    ds_and.addSample( (1,1,1) , (0,))
    net = buildNetwork(3, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_and, 3000)
    trainer.testOnData() 
    print '\n3) NOT ( (A OR B) AND C) '
    print '0 0 0  = ', net.activate((0,0,0))
    print '0 0 1  = ', net.activate((0,0,1))
    print '0 1 0  = ', net.activate((0,1,0))
    print '0 1 1  = ', net.activate((0,1,1))
    print '1 0 0  = ', net.activate((1,0,0))
    print '1 0 1  = ', net.activate((1,0,1))
    print '1 1 0  = ', net.activate((1,1,0))
    print '1 1 1  = ', net.activate((1,1,1))

if __name__ == "__main__":
   problemA()
   problemB()
   problemC()
