''' 포화 이진 트리 '''

flag = True
num = 52

def check(bnume):
    global flag

    l = len(bnume)

    if l == 1:
        return

    if bnume[l//2] == '0' and (bnume[l//2-(l//2)//2-1] == '1' or bnume[l//2+(l//2)//2+1] == "1"):
        flag = False

    check(bnume[:l//2])
    check(bnume[l//2+1:])

flag = True
bnum = bin(num)[2:]
cnt = 1
temp = 2**cnt-1

while temp < len(bnum):
    cnt += 1
    temp = 2**cnt-1

bnum = '0' * (temp - len(bnum)) + bnum

check(bnum)

if flag:
    result = 1
else:
    result = 0

print(result)