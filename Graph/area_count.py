'''
블럭을 쌓는데 블럭의 인접한 면의 수가 가장 많은 중요 블럭의 좌표를 구함
'''
import time

input = [["3"], ["1 1 1"]]

maxCount = 0
areas = {}
height = len(input) - 1
lengths = []

startTime = time.time()

for idx1, val1 in enumerate(input):
    row = ''.join(val1).replace(' ', '')
    lengRow = len(row)
    lengths.append(lengRow)

def check(width: int, col_idx:int, row_idx:int):
    global maxCount
    result = 0

    if width == 0:
        prevCol = col_idx - 1
        nextCol = col_idx + 1
        if prevCol >= 0:
            result += lengths[prevCol]
        if nextCol < height:
            result += lengths[nextCol]
        return

    if col_idx != 0 and col_idx < height and row_idx > 0 and row_idx < width:
        result = 4
    else:
        result = 3
    
    if row_idx == 0 or row_idx == width:
        result -= 1

    if maxCount <= result:
        maxCount = result

        if maxCount not in areas:
            areas[maxCount] = [(row_idx, col_idx)]
        else:
            areas[maxCount].append([row_idx, col_idx])

for i in range(len(lengths)):
    for j in range(lengths[i]):
        check(lengths[i] - 1, i, j)

endTime = time.time()

print(areas[max(areas)])
print(areas)
print(endTime - startTime)