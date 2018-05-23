#!/usr/bin/env python

import time



def readFileIntoList(fileName):
    with open(fileName) as dataFile:
        recList = [line.rstrip("\n") for line in open(fileName)]
        return recList

def parseRecList(recList):
    for i in recList:
        splitRec = i.split(",")
        print splitRec

parseRecList(readFileIntoList("2017_03_05_seed_starter_temps"))
