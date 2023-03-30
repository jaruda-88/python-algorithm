'''
블럭을 쌓는데 블럭의 인접한 몉의 수가 가장 많은 중요 블럭의 좌표를 구함
'''

input = [["3 1 2"], ["2 2 2"], ["1 3 2"]]

maxCount = 0
prevCount = 0
areas = []
width = len(input[0]) - 1
height = len(input) - 1


def check(col_idx:int, row_idx:int):
    result = 2

    if col_idx == 0 and row_idx == 0:
        return result
    elif col_idx == height and row_idx == 0:
        return result
    else:
        return result + 2

for idx1, val1  in enumerate(input):
    
    count = 0
    row = ''.join(val1)
    
    
