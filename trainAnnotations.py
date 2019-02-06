#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:57:58 2019

@author: shreyashkawalkar
"""

import os
import csv
import cv2
import numpy as np

trainPath = "/Users/shreyashkawalkar/Developer/Flipkart/trainData/"
with open('/Users/shreyashkawalkar/Developer/Flipkart/training.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    with open('/Users/shreyashkawalkar/Developer/Flipkart/trainAnnot.txt', mode='w') as employee_file:
        csv_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            filename = trainPath+row[0]
            try:
                img = cv2.imread(filename,1)
                print(img.shape)
            except:
                print("skipped")
                pass
            x1,x2,y1,y2 = row[1:5]
            filename+=" "+x1
            csv_writer.writerow([filename,y1,x2,y2])
    
        