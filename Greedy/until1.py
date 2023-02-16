'''
어떠한 수 N아 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선태갛여 수행하려고 한다. 단, 
두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
N과 K가 주어질 때 N이 1일 될 때까지 수행해야하는 최소 횟수
'''

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result +=1
    n //= k
    result += 1

# 남은 수에 대하여 횟수 체크
result += (n - 1)
print(result)