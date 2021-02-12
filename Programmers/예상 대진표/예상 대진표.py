def solution(n,a,b):
    t=1
    while True:
        if a%2==1:
            a = a//2+1
        else:
            a = a//2
        
        if b%2==1:
            b = b//2 +1
        else:
            b = b//2
        
        if a==b:
            return t
        t+=1
