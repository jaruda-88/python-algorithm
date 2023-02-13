'''
시간 복잡도
내림차순 처리 속도 비교
'''

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

startTime = time.time()

# 내림차순 정렬
for i in range(len(array)):
    minIndex = i
    for j in range(i + 1, len(array)):
        if array[minIndex] > array[j]:
            minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i] # swap

endTime = time.time()

print(f"선택 정렬 경과시간 : {round(endTime-startTime, 5)}")

array = []
for _ in range(10000):
    array.append(randint(1, 100))

startTime = time.time()

array.sort()

endTime = time.time()

print(f"기본 정렬 경과시간 : {round(endTime-startTime, 5)}")
