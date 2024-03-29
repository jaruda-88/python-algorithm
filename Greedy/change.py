'''
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수는? 단, 거슬러 줘야 할 돈 N은 항상 10의 배수.
'''

N = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    item = N // coin
    count += item
    print(f"{coin} : {item}")
    N %= coin

print("all : %s" % count)

