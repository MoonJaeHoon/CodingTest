def solution(n):
    return 1 if n==1 else 1+solution((n-1)//2) if n%2==1 else solution(n//2)