import collections

def checkVV(room1, room2, direction):
    print("checkVV")
    # 0 means going down; 1 means going up
    if direction == 0:
        # get the bottom-most row of the first room
        tmp1 = room1[-1]
        # get the top-most row of the second room
        tmp2 = room2[0]
    elif direction == 1:
        # get the top-most row of the first room
        tmp1 = room1[0]
        # get the bottom-most row of the second room
        tmp2 = room2[-1]
    print(tmp1, tmp2)
    empty1 = [pos for pos, char in enumerate(tmp1) if char == '-' or char == '|']
    empty2 = [pos for pos, char in enumerate(tmp2) if char == '-' or char == '|']

    # check if any path between room 1 and 2
    if not set(empty1).isdisjoint(empty2):
        return True
    return False



def checkHH(room1, room2):
    print("checkHH")
    # get the right-most column of the first room
    tmp1 = " "
    for line in room1:
        tmp1 += line[-1]
    # get the left-most column of the second room
    tmp2 = " "
    for line in room2:
        tmp2 += line[0]
    print(tmp1, tmp2)
    empty1 = [pos for pos, char in enumerate(tmp1) if char == '-']
    empty2 = [pos for pos, char in enumerate(tmp2) if char == '-']

    # check if any path between room 1 and 2
    if not set(empty1).isdisjoint(empty2):
        return True
    return False

def checkVH(room1, room2):
    print("checkVH")
    if checkHH(room1, room2):
        return True
    else:
        return False

def checkHV(room1, room2):
    print("checkHV")

    if checkHH(room1, room2):
        return True
    else:
        return False
