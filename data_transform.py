#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 8 18:22:47 2018

@author: Maulik
"""
import datetime

fileRead = open("soc-sign-bitcoinalpha.csv","r")
fileWrite = open("soc-sign-bitcoinalpha_updated2.csv","w")
fileWrite.write('source,target,seight\n')
for line in fileRead:
    tokens = line.split(",")
    dateOfTx = datetime.datetime.fromtimestamp(int(tokens[3])).strftime('%Y-%m-%d')
    fileWrite.write(tokens[0]+',')
    fileWrite.write(tokens[1]+',')
    fileWrite.write(tokens[2]+'\n')
    #fileWrite.write(dateOfTx+'\n')
    

fileRead.close()
fileWrite.close()
