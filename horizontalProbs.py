import sys
import os
import glob
import pickle
import random
import matplotlib.pyplot as plt

rooms = []  # list of dictionaries, each dictionary a room

def trainHorizontal(path):
    # Load Megaman horizontal rooms
    for levelFile in glob.glob(path):
        # print("Processing: " + levelFile)
        #with open(levelFile) as fp:
        fp = open(levelFile, "r")
        fp = fp.read()
        f = fp.split()
        room = {}
        for i in range(len(f)):
            room[i] = f[i]
        rooms.append(room)
            #room = {}
            #y = 0
            #for line in fp:
                #room[y] = line
                #y += 1
            #rooms.append(room)

    markovCounts = {}  # Dictionary of (x-1, y), (x-1, y+1), (x, y+1)
    for room in rooms:
        maxY = 14
        for y in range(maxY, -1, -1):
            for x in range(0, 16):
                # print("(%d, %d)"%(x,y))
                west = " "
                southwest = " "
                south = " "
                #south2 = " "
                #southeast = " "

                if x > 0:
                    west = room[y][x - 1]
                if y < maxY:
                    south = room[y + 1][x]
                if x > 0 and y < maxY:
                    southwest = room[y + 1][x - 1]
                #if y < maxY-1:
                #    south2 = room[y+2][x]
                #if x < 15 and y < maxY:
                #    southeast = room[y+1][x+1]
                key = west + south + southwest
                #key = west + southwest + south + south2 + southeast

                if not key in markovCounts.keys():
                    markovCounts[key] = {}
                if not room[y][x] in markovCounts[key].keys():
                    markovCounts[key][room[y][x]] = 0
                markovCounts[key][room[y][x]] += 1.0

    # Normalize markov counts
    markovProbabilities = {}
    for key in markovCounts.keys():
        markovProbabilities[key] = {}
        sumVal = 0
        for key2 in markovCounts[key].keys():
            sumVal += markovCounts[key][key2]
        for key2 in markovCounts[key].keys():
            markovProbabilities[key][key2] = markovCounts[key][key2] / sumVal


    #for key in markovProbabilities.keys():
    #    print(key, ": ", markovProbabilities[key])
    return markovProbabilities

def intersection(list1, list2):
    lst = [value for value in list1 if value in list2]
    return lst

def union(list1, list2):
    lst = list(set(list1) | set(list2))
    return lst

def main():
    path = "./levels_testing/horizontal/*.txt"
    path1 = "./levels_testing/horizontal1/*.txt"
    markov = trainHorizontal(path)
    markov1 = trainHorizontal(path1)
    commonKeys = intersection(markov.keys(), markov1.keys())
    result = []
    result1 = []
    x_axis = []
    x_count = 0
    difference = 0
    for key in commonKeys:
        allkeys = union(markov[key].keys(), markov1[key].keys())
        for key2 in allkeys:
            if key2 not in markov[key].keys():
                markov[key][key2] = 0
            if key2 not in markov1[key].keys():
                markov1[key][key2] = 0
            result.append(markov[key][key2])
            result1.append(markov1[key][key2])
            difference += (markov[key][key2] - markov1[key][key2]) ** 2
            x_axis.append(x_count)
            x_count += 1
        #print(key, ": ", markov[key])
        #print(key, ": ", markov1[key])
    print(result)
    print(result1)
    # difference is 0.5550917440467991
    print(difference)

    #plt.plot(x_axis, result, "r", x_axis, result1, "b-.")
    #plt.show()
main()
