'''
This program trains overall layout for a level
Input: level data of vertical, horizontal and null rooms
Output: genrated level layout
'''

import glob
import random

levels = []#list of dictionaries, each dictionary a level

#Load SMB Levels
for levelFile in glob.glob("./MegaMan_Processed_Levels/Level_with_null/*.txt"):
# for levelFile in glob.glob("./MegaMan_Processed_Levels/Level_with_null/horizontal_level_only/*.txt"):
    # print ("Processing: "+levelFile)
    # print(levelFile)
    with open(levelFile) as fp:
        level = {}
        y = 0
        for line in fp:
            level[y] = line.rstrip("\n")
            y+=1
        levels.append(level)
# print(levels)

markovCounts = {}# Dictionary of (x-1, y), (x-1, y+1), (x, y+1)
for level in levels:
    maxY = len(level)-1
    for y in range(maxY, -1, -1):
        for x in range(0, len(level[y])):
            west = " "
            southwest = " "

            if x>0:
                west = level[y][x-1]
            if x>0 and y<maxY:
                southwest = level[y+1][x]

            key = west+southwest

            if not key in markovCounts.keys():
                markovCounts[key] = {}
            if not level[y][x] in markovCounts[key].keys():
                markovCounts[key][level[y][x]] = 0
                markovCounts[key][level[y][x]] +=1.0

#Normalize markov counts
markovProbabilities = {}
for key in markovCounts.keys():
	markovProbabilities[key] = {}
	sumVal = 0
	for key2 in markovCounts[key].keys():
		sumVal+=markovCounts[key][key2]
	for key2 in markovCounts[key].keys():
		markovProbabilities[key][key2] =markovCounts[key][key2]/sumVal

# print(markovProbabilities)


'''
Generate 4X20 map layout
'''
maxY = 5
maxX = 6

for i in range(20):
    for y in range(maxY, -1, -1):
        level[y] =""
        for x in range(0, maxX):
            west = " "
            southwest = " "
            if x>0:
                west = level[y][x-1]
            if x>0 and y<maxY:
                southwest = level[y+1][x]

            key = west+southwest

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

    f = open("./MegaMan_Processed_Levels/Level_with_null/generated/generated-I2.txt", "a")
    for row in level:
        f.write(str(level[row])+'\n')
    f.write('\n')
    f.close()

    print('----------')
    for row in level:
        print(level[row])
