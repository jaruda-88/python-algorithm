'''
체스판과 같은 8 * 8 좌표 평면이다, 특정한 한 칸에 나이트가 서 있다. L자 형태로만 이동할 수 있으며 판 밖으로는 나갈 수 없다.
나이트가 이동 할 수 있는 경우의 수를 출력하는 프로그램
행은 1~8로 표현 열은 a~h로 표현 
입력 문자는 a1과같이 열과 행으로 표현
'''

ROWS = (1, 8)
COLUMNS = (1, 8)
inputData = input()
row = int(inputData[1])
column = int(ord(inputData[0])) - int(ord('a')) + 1

steps = [ (-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2) ]

result = 0

for step in steps:
    nextRow = row + step[0]
    nextColumn = column + step[1]

    if nextRow >= ROWS[0] and nextRow <= ROWS[1] and nextColumn >= COLUMNS[0] and nextColumn <= COLUMNS[1]:
        result += 1

print(result)
