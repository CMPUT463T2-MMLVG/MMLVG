for l in range(1, 86):
    new_level = []
    with open("horizontal/" + str(l) + ".txt") as fp:
        for line in fp:
            new_level.append(line)

    upper = open("horizontal_upper/" + str(l) + ".txt", "w")
    middle = open("horizontal_middle/" + str(l) + ".txt", "w")
    lower = open("horizontal_lower/" + str(l) + ".txt", "w")

    for i in range(0, 5):
        upper.write(new_level[i])

    for i in range(5, 10):
        middle.write(new_level[i])

    for i in range(10, 15):
        lower.write(new_level[i])
