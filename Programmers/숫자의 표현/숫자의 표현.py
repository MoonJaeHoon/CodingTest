# 완탐 : 정확성과 효율성 모두 성공
def solution(n):
    answer, i = 0, 1
    while i<=n//2:
        value=0
        for variable in range(i,n//2+2):
            value+=variable
            if value==n:
                answer+=1
                break
            elif value>n:
                break
        i+=1
    return answer+1





# 재귀 : 정확성 성공, 효율성 실패한 코드
'''answer=0
def recursive(n,upper_bound):
    global answer
    value=0
    for i in range(upper_bound,0,-1):
        value+=i
        if i==1:
            if n==value:
                answer+=1
                return
            else:
                return
        else:
            if n<value:
                return recursive(n,upper_bound-1)
            elif n==value:
                answer+=1
                return recursive(n,upper_bound-1)
                
def solution(n):
    recursive(n,n//2+2)
    return answer+1'''