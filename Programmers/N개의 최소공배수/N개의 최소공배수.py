# 첫번째 풀이, 효율성 좋지 못함.
'''def solution(arr):
    maximum, i= max(arr), 1
    LCM = maximum
    while not all(LCM%i==0 for i in arr):
        i+=1
        LCM = maximum*i
    return LCM'''

# 두번째 풀이, 최대공약수를 활용하였음 효율성 면에서 우월함.
from math import gcd
def solution(arr):
    LCM = arr[0]
    for n in arr[1:]:
        LCM = LCM*n // gcd(LCM,n)
    return LCM