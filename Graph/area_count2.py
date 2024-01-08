'''
블럭을 쌓는데 블럭의 인접한 면의 수가 가장 많은 중요 블럭의 좌표를 구함
'''

import time

input = [["2 2 2"], ["3 1 2"], ["2 1 3"]]

maxCount = 0
result = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
blocks = []

starttime = time.time()

for idx1, val1 in enumerate(input):
    row = ''.join(val1).replace(' ', '')
    lengRow = len(row)
    blocks.append(lengRow)

height = len(blocks)
col = 0

while col < height:
    cnt = 0

    width = blocks[col]

    row = 0
    while row < width:
        cnt = 0
        
        prevRow = row - 1
        nextRow = row + 1

        prevCol = col - 1
        nextCol = col + 1

        if prevRow < 0 and nextRow >= width:
            if prevCol >= 0:
                cnt += blocks[prevCol]
            if nextCol < height:
                cnt += blocks[nextCol]
        else:
            if prevRow >= 0:
                cnt += 1
            if nextRow < width:
                cnt += 1

            if prevCol >= 0:
                cnt += 1
            if nextCol < height:
                cnt += 1

        if maxCount <= cnt:
            maxCount = cnt
            result[maxCount].append((row, col))

        row += 1

    col += 1

endTime = time.time()

print(result[maxCount])

print(endTime - starttime)