''' 상하좌우 알고리즘 '''

park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]
ditections = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}

height, width = len(park), len(park[0])

start = None
for i in range(height):
    for j in range(width):
        if park[i][j] == "S":
            start = (i, j)
            break
    if start is not None:
        break

curPos = start

for route in routes:
    dir, dist = route[0], int(route[2])
    dx, dy = ditections[dir] 

    pos = (curPos[0] + dx * dist, curPos[1] + dy * dist)

    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        isblock = False

        for d in range(dist):
            checkPos = (curPos[0] + dx * (d + 1), curPos[1] + dy * (d + 1))
            print(checkPos, park[checkPos[0]][checkPos[1]])
            if park[checkPos[0]][checkPos[1]] == "X":
                isblock = True
                break 

        if not isblock:
            curPos = pos

print(list(curPos))