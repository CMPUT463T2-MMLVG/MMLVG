import sys
import os
import glob
import pickle
import random

rooms = []  # list of dictionaries, each dictionary a room

def trainHorizontal():
    # Load Megaman horizontal rooms
    for levelFile in glob.glob("./new_levels/horizontal/*.txt"):
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

    room = {}
    maxY = 14
    maxX = 16

    for y in range(maxY, -1, -1):
        room[y] = ""
        for x in range(0, maxX):
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

            if key in markovProbabilities.keys():
                randomSample = random.uniform(0, 1)
                currValue = 0.0
                for key2 in markovProbabilities[key]:
                    if randomSample >= currValue and randomSample < currValue + markovProbabilities[key][key2]:
                        room[y] += key2
                        break
                    currValue += markovProbabilities[key][key2]
            else:
                room[y] += "-"
    new_room = []
    for y in range(0, maxY + 1):
        new_room.append(room[y])
        # new_room += "\n"
    return new_room
