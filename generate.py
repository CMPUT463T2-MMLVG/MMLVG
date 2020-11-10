import sys
import os
import random
import pickle

markovProbabilities = pickle.load(open("smbprobabilities.pickle", "rb"))

level = {}

maxY = 14
maxX = 100

for y in range(maxY, -1, -1):
	level[y] =""
	for x in range(0, maxX):
		west = " "
		southwest = " "
		south = " "

		if x>0: 
			west = level[y][x-1]
		if y<maxY: 
			south = level[y+1][x-1]
		if x>0 and y<maxY: 
			southwest = level[y+1][x]

		key = west+southwest+south

		if key in markovProbabilities.keys():
			randomSample = random.uniform(0, 1)
			currValue = 0.0
			for key2 in markovProbabilities[key]:
				if randomSample>=currValue and randomSample<currValue+markovProbabilities[key][key2]:
					level[y] += key2
					break
				currValue+=markovProbabilities[key][key2]
		else:
			level[y] +="-"

with open("./Generated Levels/output.txt", "a") as the_file:
	for y in range(0, maxY+1):
   		the_file.write(level[y]+"\n")
