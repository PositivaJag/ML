# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:20:12 2021
Kalle
@author: Jenni
"""

import SVM
from matplotlib import pyplot

Indata = {1: [[1, 7], [2, 8], [3, 8]], -1: [[5, 1], [6, -1], [7, 3]]}
# Indata = {1: [[55, 28],
#   [47, 24],
#   [47, 23],
#   [45, 11],
#   [50, 25],
#   [55, 27],
#   [54, 27],
#   [47, 26],
#   [50, 17],
#   [50, 17]],
#   -1: [[39, 0],
#   [42, 21],
#   [34, 17],
#   [39, 13],
#   [38, 15],
#   [42, 18],
#   [36, 14],
#   [38, 15],
#   [36, 16],
#   [34, 17]]}



S = SVM.SVM(Indata)

(meanClass1, meanClass2) = S.calcMeanPerClass()

distMeansPerClass = S.calcDistance(meanClass1, meanClass2)

(k, m) = S.calcLineEquation(meanClass1, meanClass2)

k2 = S.calcNormal(k)

(norm1, norm2) = S.calcPointsFromEquation(k2, m)





#Print all 
#Print points
pyplot.scatter(S.points1[0], S.points1[1], s = 15, c = 'b')
pyplot.scatter(S.pointsMinus1[0], S.pointsMinus1[1], s = 15, c = 'r')

#print mean class points
# pyplot.scatter(S.meanPoints[0], S.meanPoints[1], s = 40, c = 'black', marker = '*')
#Print line between mean points
# pyplot.plot(S.meanPoints[0], S.meanPoints[1])
pyplot.plot([norm1[0], norm2[0]], [norm1[1], norm2[1]])


pyplot.show

(k, m) = S.calcLineEquation(S.meanPoints[0], S.meanPoints[1])

print("medellinjens k och m är ", round(k, 2), round(m, 2))


