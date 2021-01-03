# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:17:20 2021

@author: Jenni
"""


import numpy as np
from matplotlib import image
from matplotlib import pyplot
import os
import random
from PIL import Image
import math


class SVM:
    def __init__(self, points):
        self.points = points
        self.meanPoints = []
        self.X = [[],[]]
        self.Y =[]
        
        x = []
        y = []
        for L in points[1]:
            x.append(L[0])
            y.append(L[1])
            self.X[0].append(L[0])
            self.X[1].append(L[1])
            self.Y.append(1)
        self.points1 = [x, y]
        
        
        x = []
        y = []
        for L in points[-1]:
            x.append(L[0])
            y.append(L[1])
            self.X[0].append(L[0])
            self.X[1].append(L[1])
            self.Y.append(-1)
        self.pointsMinus1 = [x, y]
        
                
        self.minx = min([min(self.points1[0]), min(self.pointsMinus1[0])])
        self.maxx = max([max(self.points1[0]), max(self.pointsMinus1[0])])
        self.miny = min([min(self.points1[1]), min(self.pointsMinus1[1])])
        self.maxy = max([max(self.points1[1]), max(self.pointsMinus1[1])])
        self.rangePoints = [[self.minx, self.miny], [self.maxx, self.maxy]]


        
    def printPoints(self):
        
        pyplot.scatter(self.points1[0], self.points1[1], s = 15, c = 'b')
        pyplot.scatter(self.pointsMinus1[0], self.pointsMinus1[1], s = 15, c = 'r')
        if self.meanPoints != []:
            pyplot.scatter(self.meanPoints[0], self.meanPoints[1], s = 40, c = 'black', marker = '*')
            pyplot.plot(self.meanPoints[0], self.meanPoints[1])
        pyplot.show
        
        (k, m) = self.calcLinjensEkvation(self.meanPoints[0], self.meanPoints[1])
        
        print("medellinjens k och m är ", round(k, 2), round(m, 2))
        
    def calcMeanPoints(self, list):
        """
        Input: list wit x and y coordinates [[x], [y]]
        """
        X = sum(list[0])/len(list[0])
        Y = sum(list[1])/len(list[1])
        
        return([X, Y])
    
    def calcDistance(self, p1, p2):
        """
        Input: 
        a list with two points in it [[x, y],[X, Y]]
        """
        dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]+p2[1])**2)
        return (dist)
        

    def calcMeanPerClass(self):
        
        mean1 = self.calcMeanPoints(self.points1)
        mean2 = self.calcMeanPoints(self.pointsMinus1)
        self.meanPoints = [[mean1[0], mean2[0]], [mean1[1], mean2[1]]]
        print("Mean points per class calculated")
        return([mean1[0], mean1[1]], [mean2[0], mean2[1]])

        
    def printTwoPointLine(self, listX, listY):
        pyplot.plot(listX, listY)
        pyplot.show
        
    def calcLineEquation(self, p1, p2):
        x0 = p1[0]
        x1 = p2[1]
        y0 = p1[0]
        y1 = p2[1]
        
        #y = kx+m
        k = (y1-y0)/(x1-x0)
        
        # y = k(x-x1)+y1
        # y = kx-kx1+y1 => m = k*x1+y1
        m = (k*-x0)+y0
        
        return([k, m])
    
    def calcNormal(self, k):
        return(1/k)

    
    def calcPointsFromEquation(self, k, m):
        p1 = k* self.minx + m
        p2 = k* self.maxx + m
        
        return([[self.minx,p1], [self.maxx,p2]])
    
    def createW(self):
        self.w = []
        for r in range(0, len(self.X)):
            w.append(random.random())
        
    
    # def calcDistToLine(self):
        
    #     for p in [self.points1, self.pointsMinus1]:
            
        
        
        