def solution(n):
    answer = ''
    while True:
        n-=1
        R = n%3
        if R==0:
            answer = '1'+answer
        elif R==1:
            answer = '2'+answer
        elif R==2:
            answer = '4'+answer
        n = n//3
        if n==0:
            break
    return answer