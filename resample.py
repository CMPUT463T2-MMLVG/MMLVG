import random
from trainH_1 import trainHorizontal
# from assembleHorizontal import trainHorizontal
from trainV_1 import trainVertical
from utils import checkHH, checkVH, checkVV, checkHV

layout_ls = []
with open("Generated Levels/layout.txt") as fp:
    for line in fp:
        layout_ls.append(line.replace("\n", ""))

num = 6

countH = layout_ls[num].count("H")
countV = layout_ls[num].count("V")
print(countH, countV)
layout = list(layout_ls[num])
x = 1
y = 1

layout_axis = [[1, 1]]  # initialize the origin point: use (1,1) instead of (0,0) for future calculation
lowest_y = 1

height = 1
width = 1

for i in range(1, 16):
    if layout[i] == "V" and layout[i - 1] == "V":
        if i == 1 or layout[i - 2] == "H":
            direction = random.randint(0, 1)  # 0 means going down; 1 means going up

        if direction == 0:
            y += 1
            height = y
        else:
            y -= 1
            lowest_y = y

    else:
        x += 1
        width = x

    layout_axis.append([x, y])

if lowest_y < 1:
    for i in range(len(layout_axis)):
        layout_axis[i][1] += abs(lowest_y - 1)
        if height < layout_axis[i][1]:
            height = layout_axis[i][1]
print(layout_axis)
print(layout)
width *= 16
height *= 15

map = "@" * width
map = [map] * height  # map with only null tiles

last_room = 0
i = 0
while  (i < len(layout)):
    x1 = layout_axis[i][0] * 16 - 16
    x2 = layout_axis[i][0] * 16
    y1 = layout_axis[i][1] * 15 - 15

    if layout[i] == "V":
        room = trainVertical()
        if i > 0 and layout[i-1] == "H":
            if not checkHV(last_room, room):
                continue
        elif i>0 and layout[i-1] == "V":
            # check direction
            # if going up, direction = 1; if going down, direction=0
            if layout_axis[i][1] > layout_axis[i-1][1]:
                direction = 1
            else:
                direction = 0
            if not checkVV(last_room, room, direction):
                continue
    else:
        room = trainHorizontal()
        if i > 0 and layout[i-1] == "H":
            if not checkHH(last_room, room):
                continue
        elif  i>0 and layout[i-1] == "V":
            if not checkVH(last_room, room):
                continue

    print(y1,x1,x2)
    # print(room)
    last_room = room
    for line in room:
        map[y1] = map[y1][:x1] + line.replace("\n", "") + map[y1][x2:]
        # print(map[y1])
        y1 += 1
    print(y1,x1,x2)
    i += 1

    # i = len(layout)



fp = open("Generated Levels/result.txt", "w")
for i in range(len(map)):
    fp.write(map[i] + "\n")
