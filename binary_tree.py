import os


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
        # 2*(size + 1) -1
        binaryTreeSize = (binaryTreeSize + 1) * 2 - 1
    
    binaryNumber = "0" * (binaryTreeSize - len(binaryNumber)) + binaryNumber
    # ------------ 포화 이진트리
    return binaryNumber

print(number_to_perfect_binary_tree(7))