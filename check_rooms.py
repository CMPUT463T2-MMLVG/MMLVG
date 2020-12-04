import collections


def check_HH(roomH, roomPrev):
    leftTiles = " "
    rightTiles = " "
    for line in roomH:
        leftTiles += line[0]
        rightTiles += line[-1]
    leftEmpty = [pos for pos, char in enumerate(
        leftTiles) if pos < 13 and char == '-' or char == '|']
    rightEmpty = [pos for pos, char in enumerate(
        rightTiles) if pos < 13 and char == '-' or char == '|']
    if not leftEmpty or not rightEmpty:
        return False
    prevTiles = " "
    for line in roomPrev:
        prevTiles += line[-1]
    prevEmpty = [pos for pos, char in enumerate(
        prevTiles) if pos < 13 and char == '-' or char == '|']
    # if find path return True else False
    return not set(leftEmpty).isdisjoint(prevEmpty)


def check_VV(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    topTiles = " "
    bottomTiles = " "
    topTiles = roomV[0]
    bottomTiles = roomV[-1]
    topEmpty = [pos for pos, char in enumerate(
        topTiles) if char == '-' or char == '|']
    bottomEmpty = [pos for pos, char in enumerate(
        bottomTiles) if char == '-' or char == '|']
    if not bottomEmpty or not topEmpty:
        return False
    prevTiles = " "
    if not direction:
        prevTiles = roomPrev[-1]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
        # print(topEmpty, prevEmpty)
        return not set(topEmpty).isdisjoint(prevEmpty)
    else:
        prevTiles = roomPrev[0]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
        # print(bottomEmpty, prevEmpty)
        return not set(bottomEmpty).isdisjoint(prevEmpty)


def check_HV(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    leftTiles = " "
    for line in roomV:
        leftTiles += line[0]
    leftEmpty = [pos for pos, char in enumerate(
        leftTiles) if pos < 13 and char == '-' or char == '|']
    marginTiles = " "
    if not direction:
        marginTiles = roomV[-1]
        marginEmpty = [pos for pos, char in enumerate(
            marginTiles) if char == '-' or char == '|']
    else:
        marginTiles = roomV[0]
        marginEmpty = [pos for pos, char in enumerate(
            marginTiles) if char == '-' or char == '|']
    if not leftEmpty or not marginEmpty:
        return False
    prevTiles = " "
    for line in roomPrev:
        prevTiles += line[-1]
    prevEmpty = [pos for pos, char in enumerate(
        prevTiles) if pos < 13 and char == '-' or char == '|']
    # print(leftEmpty, prevEmpty)
    return not set(leftEmpty).isdisjoint(prevEmpty)


def check_VH(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    rightTiles = " "
    for line in roomV:
        rightTiles += line[-1]
    rightEmpty = [pos for pos, char in enumerate(
        rightTiles) if pos < 13 and char == '-' or char == '|']
    marginTiles = " "
    prevTiles = " "
    if not direction:
        # roomV ceiling line
        marginTiles = roomV[0]
        marginEmpty = [pos for pos, char in enumerate(
            marginTiles) if char == '-' or char == '|']
        prevTiles = roomPrev[-1]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
    else:
        marginTiles = roomV[-1]
        marginEmpty = [pos for pos, char in enumerate(
            marginTiles) if char == '-' or char == '|']
        prevTiles = roomPrev[0]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
    if not rightEmpty or not marginEmpty:
        return False
    return not set(marginEmpty).isdisjoint(prevEmpty)


room1 = []
room2 = []
with open("test_resample/v_b_r_good.txt") as fp:
    for line in fp:
        room1.append(line.replace("\n", ""))
with open("test_resample/v_good.txt") as fp:
    for line in fp:
        room2.append(line.replace("\n", ""))

print(check_HV(room2, room1, 0))