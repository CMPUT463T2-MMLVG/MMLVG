import os

level = {}
# file path
for l in range(1,11):
    with open("levels/megaman_1_"+ str(l) +".txt") as fp:
        y = 0
        for line in fp:
            level[y] = line.replace("\n","")
            y += 1

    x = len(line)

    if x % 16 != 0:
        hor_chunks_num = int(x / 16) + 1
        x = hor_chunks_num * 16
    else:
        hor_chunks_num = int(x / 16)

    hor_chunks = []
    for i in range(1, hor_chunks_num + 1):
        hor_chunks.append([16 * (i - 1), 16 * i])

    if y % 15 != 0:
        ver_chunks_num = int(y / 15) - 1
    else:
        ver_chunks_num = int(y / 15)

    ver_chunks = []
    for i in range(1, ver_chunks_num + 1):
        ver_chunks.append([y - 15 * i, y - 15 * (i - 1)])

    null_tiles = []
    for i in range(ver_chunks_num):
        for j in range(hor_chunks_num):
            f = open("newlevels/" + str(l) + "/V" + str(i) + "H" + str(j) + ".txt", "w")
            for m in range(ver_chunks[i][0], ver_chunks[i][1]):
                f.write(level[m][hor_chunks[j][0]:hor_chunks[j][1]] + "\n")
                if "@" in level[m][hor_chunks[j][0]:hor_chunks[j][1]]:
                    null_tiles.append(str(i) + "," + str(j))

    null_tiles = [[i, null_tiles.count(i)] for i in set(null_tiles)]
    for i in range(len(null_tiles)):
        if null_tiles[i][1] == 15:
            ls = null_tiles[i][0].split(",")
            path = "newlevels/" + str(l) + "/V" + str(ls[0]) + "H" + str(ls[1]) + ".txt"
            if os.path.exists(path):
                os.remove(path)

