def solution(arr1, arr2):
    arr2 = [ [arr2[row][column] for row in range(len(arr2)) ] for column in range(len(arr2[0]))]
    return [ [sum([i*j for i,j in zip(row,column)]) for column in arr2] for row in arr1]

## 다른 풀이
# zip(*B) 는 B의 열을 행처럼 바꿔주는 방법이라고 함. Transpose와 그 기능이 비슷한 듯 하다.
'''def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]'''