import collections
from collections import deque

def check_HH(roomH, roomPrev):
    leftTiles = " "
    rightTiles = " "
    start = []
    end = []
    for line in roomH:
        leftTiles += line[0]
        rightTiles += line[-1]
    leftEmpty = [pos for pos, char in enumerate(
        leftTiles) if pos < 13 and char == '-' or char == '|']
    rightEmpty = [pos for pos, char in enumerate(
        rightTiles) if pos < 13 and char == '-' or char == '|']
    if not leftEmpty or not rightEmpty:
        return False
    #for pos in leftEmpty:
    #    start.append([pos,0])
    for pos in rightEmpty:
        end.append([pos,15])
    prevTiles = " "
    for line in roomPrev:
        prevTiles += line[-1]
    prevEmpty = [pos for pos, char in enumerate(
        prevTiles) if pos < 13 and char == '-' or char == '|']
    if set(leftEmpty).isdisjoint(prevEmpty):
        return False
    else:
        empties = set(leftEmpty).intersection(prevEmpty)
        for pos in empties:
            start.append([pos,0])
        if not findPath(roomH, start, end):
            return False
    # if find path return True else False
    return True


def check_VV(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    topTiles = " "
    bottomTiles = " "
    start = []
    end = []
    topTiles = roomV[0]
    bottomTiles = roomV[-1]
    topEmpty = [pos for pos, char in enumerate(
        topTiles) if char == '-' or char == '|']
    bottomEmpty = [pos for pos, char in enumerate(
        bottomTiles) if char == '-' or char == '|']
    if not bottomEmpty or not topEmpty:
        return False
    #for pos in topEmpty:
    #    start.append([0,pos])
    #for pos in bottomEmpty:
    #    end.append([14,pos])
    #if not findPath(roomV, start, end):
    #    return False
    prevTiles = " "
    if not direction:
        prevTiles = roomPrev[-1]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
        # print(topEmpty, prevEmpty)
        if set(topEmpty).isdisjoint(prevEmpty):
            return False
        else:
            empties = set(topEmpty).intersection(prevEmpty)
            for pos in empties:
                start.append([0,pos])
            for pos in bottomEmpty:
                end.append([14,pos])
            if not findPath(roomV, start, end):
                return False
    else:
        prevTiles = roomPrev[0]
        prevEmpty = [pos for pos, char in enumerate(
            prevTiles) if char == '-' or char == '|']
        # print(bottomEmpty, prevEmpty)
        if set(bottomEmpty).isdisjoint(prevEmpty):
            return False
        else:
            empties = set(bottomEmpty).intersection(prevEmpty)
            for pos in empties:
                start.append([14,pos])
            for pos in topEmpty:
                end.append([0,pos])
            if not findPath(roomV, start, end):
                return False
    return True


def check_HV(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    leftTiles = " "
    start = []
    end = []
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
    #for pos in leftEmpty:
    #    start.append([pos,0])
    for pos in marginEmpty:
        if not direction:
            end.append([14,pos])
        else:
            end.append([0,pos])
    #if not findPath(roomV, start, end):
    #    return False
    prevTiles = " "
    for line in roomPrev:
        prevTiles += line[-1]
    prevEmpty = [pos for pos, char in enumerate(
        prevTiles) if pos < 13 and char == '-' or char == '|']
    # print(leftEmpty, prevEmpty)
    if set(leftEmpty).isdisjoint(prevEmpty):
        return False
    else:
        empties = set(leftEmpty).intersection(prevEmpty)
        print("empties:")
        print(empties)
        for pos in empties:
            start.append([pos,0])
        if not findPath(roomV, start, end):
            return False
    return True


def check_VH(roomV, roomPrev, direction):
    # 0 means going down; 1 means going up
    rightTiles = " "
    start = []
    end = []
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
    #for pos in marginEmpty:
    #    if not direction:
    #        start.append([0,pos])
    #    else:
    #        start.append([14,pos])
    for pos in rightEmpty:
        end.append([pos,15])
    #if not findPath(roomV, start, end):
    #    return False
    if set(marginEmpty).isdisjoint(prevEmpty):
        return False
    else:
        empties = set(marginEmpty).intersection(prevEmpty)
        print("empties:")
        print(empties)
        for pos in empties:
            if not direction:
                start.append([0,pos])
            else:
                start.append([14,pos])
        if not findPath(roomV, start, end):
            return False
    return True


def findPath(room, emptyFrom: list, emptyTo: list):
    visited = []
    stack = deque()
    for i in emptyFrom:
        stack.append(i)
    while (len(stack) != 0):
        s = stack.pop()
        #print(s)
        visited.append(s)
        if s in emptyTo:
            return True
        neighbors = availableNeighbor(room, s)
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return False


def availableNeighbor(room, position):
    neighbors = []
    i = position[0]
    j = position[1]
    if i > 0 and (room[i-1][j] == '-' or room[i-1][j] == '|'):
        neighbors.append([i-1,j])
    if j > 0 and (room[i][j-1] == '-' or room[i][j-1] == '|'):
        neighbors.append([i,j-1])
    if i < 14 and (room[i+1][j] == '-' or room[i+1][j] == '|'):
        neighbors.append([i+1,j])
    if j < 15 and (room[i][j+1] == '-' or room[i][j+1] == '|'):
        neighbors.append([i,j+1])
    return neighbors


""" room1 = []
room2 = []
with open("test_resample/v_b_r_good.txt") as fp:
    for line in fp:
        room1.append(line.replace("\n", ""))
with open("test_resample/v_good.txt") as fp:
    for line in fp:
        room2.append(line.replace("\n", ""))

print(check_HV(room2, room1, 0)) """
