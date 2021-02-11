def solution(s):
    t, remove_count = 0, 0
    while s!='1':
        count0 = s.count('0')
        remove_count += count0
        s = format(len(s)-count0,'b')
        t+=1
    return [t,remove_count]