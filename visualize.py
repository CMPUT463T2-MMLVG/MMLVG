import sys
import os
import glob
from PIL import Image

# Load sprites
sprites = {}
for filename in glob.glob("./tiles/*.png"):
    im = Image.open(filename)
    splits = filename.split("/")
    name = splits[-1][:-4]
    sprites[name] = im

visualization = {}
visualization["@"] = "null"
visualization["#"] = "solid"
visualization["-"] = "empty"
visualization["B"] = "super_arm_block"
visualization["H"] = "spikes"
visualization["|"] = "ladder"
visualization["L"] = "large_health"
visualization["l"] = "small_health"
visualization["W"] = "large_weapon_energy"
visualization["w"] = "small_weapon_energy"
visualization["+"] = "extra_life"
visualization["M"] = "moving_platform"
visualization["P"] = "player"
visualization["C"] = "shooter"
visualization["D"] = "boss_door"
visualization["U"] = "beam"
visualization["t"] = "undefined"
visualization["*"] = "special_item"

# Visualize Output Level
level = {}
# file path
with open("./TestFile.txt") as fp:
    y = 0
    for line in fp:
        level[y] = line
        y += 1

image = Image.new("RGB", (3000, 3000), color=(81, 50, 8))
pixels = image.load()

maxY = y
maxX = len(line)

for y in range(0, maxY):
    for x in range(0, maxX):
        imageToUse = None
        if level[y][x] in visualization.keys():
            imageToUse = sprites[visualization[level[y][x]]]
        if not imageToUse == None:
            pixelsToUse = imageToUse.load()
            for x2 in range(0, 16):
                for y2 in range(0, 16):
                    if pixelsToUse[x2, y2][3] > 0:
                        pixels[x * 16 + x2, y * 16 + y2] = pixelsToUse[x2, y2][0:-1]

image.save("output.jpeg", "JPEG")
