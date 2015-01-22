##############################################
##############################################
#      Applied Data Science GX5004           # 
#      Lab 2                                 #
#      Dimas Rinarso Putro | drp354@nyu.edu  #
#      No.1b                                 #
##############################################

import pybrain
from pybrain.datasets import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def estimateAnd():
    ds_and = SupervisedDataSet(2, 1)
    ds_and = SupervisedDataSet(2, 1)
    ds_and.addSample( (0,0) , (0,))
    ds_and.addSample( (0,1) , (0,))
    ds_and.addSample( (1,0) , (0,))
    ds_and.addSample( (1,1) , (1,))
    net = buildNetwork(2, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_and, 3000)
    trainer.testOnData() 
    print '\nthe prediction for AND value:'
    print '1 AND 1 = ', net.activate((1,1))
    print '1 AND 0 = ', net.activate((1,0))
    print '0 AND 1 = ', net.activate((0,1))
    print '0 AND 0 = ', net.activate((0,0))

def estimateOr():
    ds_or = SupervisedDataSet(2, 1)
    ds_or = SupervisedDataSet(2, 1)
    ds_or.addSample( (0,0) , (0,))
    ds_or.addSample( (0,1) , (1,))
    ds_or.addSample( (1,0) , (1,))
    ds_or.addSample( (1,1) , (1,))
    net = buildNetwork(2, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_or, 3000)
    trainer.testOnData() 
    print '\nthe prediction for OR value:'
    print '1 OR 1 = ', net.activate((1,1))
    print '1 OR 0 = ', net.activate((1,0))
    print '0 OR 1 = ', net.activate((0,1))
    print '0 OR 0 = ', net.activate((0,0))

def estimateNot():
    ds_not = SupervisedDataSet(1, 1)
    ds_not.addSample( (0,) , (1,))
    ds_not.addSample( (1,) , (0,))
    net = buildNetwork(1, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_not, 3000)
    trainer.testOnData() 
    print '\nthe prediction for NOT value:'
    print 'NOT 0  = ', net.activate((0,))
    print 'NOT 1  = ', net.activate((1,))

def estimateNor():
    ds_nor = SupervisedDataSet(2, 1)
    ds_nor.addSample( (0,0) , (1,))
    ds_nor.addSample( (0,1) , (0,))
    ds_nor.addSample( (1,0) , (0,))
    ds_nor.addSample( (1,1) , (0,))
    net = buildNetwork(2, 10, 1, bias=True)
    trainer = BackpropTrainer(net, learningrate = 0.01, momentum = 0.99)
    trainer.trainOnDataset(ds_nor, 3000)
    trainer.testOnData() 
    print '\nthe prediction for NOR value:'
    print '1 NOR 1 = ', net.activate((1,1))
    print '1 NOR 0 = ', net.activate((1,0))
    print '0 NOR 1 = ', net.activate((0,1))
    print '0 NOR 0 = ', net.activate((0,0))


if __name__ == "__main__":
   estimateAnd()
   estimateOr()
   estimateNot()
   estimateNor()
