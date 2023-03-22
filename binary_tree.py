import os

number = 100

def number_to_perfect_binary_tree(number):

    reverseBinaryNumber = []

    # ------------- 16진수 2진수로 변환
    while number != 1:
        reverseBinaryNumber.append(str(number % 2))
        number //= 2
    reverseBinaryNumber.append('1')
    # ------------- 16진수 2진수로 변환

    # ------------- 포화 이진 트리
    binaryNumber = ''.join(reverseBinaryNumber[::-1])
    binaryTreeSize = 1
    while binaryTreeSize < len(binaryNumber):
        # 2*(size + 1) - 1
        binaryTreeSize = (binaryTreeSize + 1) * 2 - 1
    
    binaryNumber = "0" * (binaryTreeSize - len(binaryNumber)) + binaryNumber
    # ------------ 포화 이진트리
    return binaryNumber

def check_tree(start, end, binary_string):

    if start == end:
        return binary_string[start]

    mid = (start + end) // 2
    
    left = check_tree(start, mid - 1, binary_string)
    if not left or (binary_string[mid] == "0" and left == "1"):
        return False
    
    right = check_tree(mid + 1, end, binary_string)
    if not right or (binary_string[mid] == "0" and right == "1"):
        return False

    if left == "0" and right == "0" and binary_string[mid] == "0":
        return "0"

    return "1"

binaryStr = number_to_perfect_binary_tree(number)
result = check_tree(0, len(binaryStr) - 1, binaryStr)
print(result)