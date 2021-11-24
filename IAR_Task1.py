# -*- coding: utf-8 -*-
"""
Calculate all the possible positions of and end effector with an arm consisting of 2 straight lengths joined by a joint.
Constraints:
* Angle between L1 and ground: 0 < theta1 < pi/2
* Angle between L2 and L1:  -pi/2 < theta < pi/2
"""
 
import math
import numpy as np
 
l1 = 5
l2 = 2
 
lis = []
 
for i in range(90):
    for j in range(180):
        theta1 = math.pi*90/180
        theta2 = (j - 90)*math.pi/180
        phi = theta1 + theta2
        
        x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
        
        y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)
        
        lis.append((x,y))
arr = np.round(np.array(lis),decimals=1)
 
 
def find(arr,x):
    for i in range(arr.shape[0]):
        if x[0] == arr[i][0] and x[1] == arr[i][1]:
            return True
    return False
 
find(arr, [2., 5.1])
