''' 곡갱이 최소한의 피로도로 광물을 캐라 '''

from collections import deque

picks = [1, 3, 2] # 다이아 곡갱이 1개, 철 곡갱이 3개, 돌 곡갱이 1개, 0 <= pick <= 5
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]    # 5 <= mineral <= 50
mineralType = { "diamond": 0, "iron": 1, "stone": 2} # 곡갱이 종류
fatigueList = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]    # diamond, iron, stone ex) 철 곡갱이로 다이아를 캘 때 5, 철 1, 돌 1
maxUsage = 5    # 광물을 5개 캔 후 더 이상 사용할 수 없다

minerals = minerals[:maxUsage * sum(picks)]

q = deque(minerals)

digs = []
while q:
    digCount = 0
    usedDia, usedIron, usedStone = 0, 0, 0
    while digCount < 5:
        digCount += 1
        mineral = q.popleft()
        usedDia += fatigueList[0][mineralType[mineral]]
        usedIron += fatigueList[1][mineralType[mineral]]
        usedStone += fatigueList[2][mineralType[mineral]]
        if not q:
            break
    digs.append([usedDia, usedIron, usedStone])

digs.sort(key = lambda x : [x[2], x[1], x[0]])

result = 0
for idx, pick in enumerate(picks):
    for _ in range(pick):
        if digs:
            result += digs.pop()[idx]

print(result)