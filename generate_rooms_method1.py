import random
from trainH_1 import trainHorizontal
# from assembleHorizontal import trainHorizontal
from trainV_1 import trainVertical
from check_rooms import check_HH, check_VH, check_VV, check_HV

layout_ls = []
# for i in range(1, 19):
for l in range(1, 19):
    level =  open("./MegaMan_Processed_Levels/level_structure_method1/"+str(l)+".txt", "r").read()
    rows = level.split('\n')[:-1]
    rows.reverse()
    print(rows)

    # record coordinate for each H/V room
    layout_axis = []
    # record H/V room
    layout = []
    for j in range(len(rows)):
        for k in range(len(rows[j])):
            room = rows[j][k]
            if room == "H" or room == "V":
                layout.append(room)
                layout_axis.append([j+1, k+1])
    print(layout)
    print(layout_axis)

    height = 5
    width = 5

    width *= 16
    height *= 15

    map = "@" * width
    map = [map] * height  # map with only null tiles

    H = 1
    V = 1
    for i in range(len(layout)):
        x1 = layout_axis[i][0] * 16 - 16
        x2 = layout_axis[i][0] * 16
        y1 = layout_axis[i][1] * 15 - 15

        if layout[i] == "V":
            room = trainVertical()
            V += 1

        else:
            room = trainHorizontal()
            H += 1
        # print(fp.read())
        # print(y1,x1,x2)
        for line in room:
            # print(line)
            map[y1] = map[y1][:x1] + line.replace("\n", "") + map[y1][x2:]
            y1 += 1

    fp = open("Generated Levels/Levels_Method1/result"+str(l)+".txt", "w")
    for i in range(len(map)):
        fp.write(map[i] + "\n")
