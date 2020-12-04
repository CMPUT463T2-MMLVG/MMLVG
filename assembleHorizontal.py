from trainHorizontalLower import trainHorizontalLower
from trainHorizontalUpper import trainHorizontalUpper
from trainHorizontalMiddle import trainHorizontalMiddle

# for l in range(1, 50):
#     upper = open("output/horizontal_upper/output" + str(l) + ".txt")
#     middle = open("output/horizontal_middle/output" + str(l) + ".txt")
#     lower = open("output/horizontal_lower/output" + str(l) + ".txt")
#
#     assembled = open("output/horizontal_assembled/" + str(l) + ".txt", "w")
#
#     for line in upper:
#         assembled.write(line)
#     for line in middle:
#         assembled.write(line)
#     for line in lower:
#         assembled.write(line)
upper = trainHorizontalUpper()
lower = trainHorizontalLower()
middle = trainHorizontalMiddle()
print(upper, lower, middle)
room = []
for line in upper:
    room.append(line)
for line in middle:
    room.append(line)
for line in lower:
    room.append(line)
# return room
