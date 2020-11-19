import glob
import random

markovCounts = {}
levels = []

for levelFile in glob.glob("./MegaMan_Processed_Levels/1-*/path.txt"):
	print("Processing: "+levelFile)
	with open(levelFile) as fp:
		sequence = fp.readline()
		sequenceText = "".join(c for c in sequence if c.isalpha())
		levels.append(sequenceText)
print(levels)

for level in levels:
	sequence = list(level)
	#print(sequence)
	for i in range(1, len(sequence)):
		if not sequence[i-1] in markovCounts.keys():
			markovCounts[sequence[i-1]] = {}
		if not sequence[i] in markovCounts[sequence[i-1]].keys():
			markovCounts[sequence[i-1]][sequence[i]] = 0
		markovCounts[sequence[i-1]][sequence[i]] += 1.0

markovProbabilities = {}
for key in markovCounts.keys():
	markovProbabilities[key] = {}
	sumVal = 0
	for key2 in markovCounts[key].keys():
		sumVal+=markovCounts[key][key2]
	for key2 in markovCounts[key].keys():
		markovProbabilities[key][key2] =markovCounts[key][key2]/sumVal
print(markovCounts)
print(markovProbabilities)

result = []
for i in range(20):
	sequence = ""
	randomFirst = random.uniform(0,1)
	if randomFirst >= 0.5:
		firstRoom = "V"
	else:
		firstRoom = "H"
	sequence += firstRoom
	for j in range(15):
		randomSample = random.uniform(0,1)
		if randomSample <= min(markovProbabilities[firstRoom].values()):
			thisRoom = "H" if firstRoom == "V" else "V"
		else:
			thisRoom = firstRoom
		sequence += thisRoom
		firstRoom = thisRoom
	result.append(sequence)
print(result)