## 모두 통과는 했지만, 효율성 측면에서 좋지 않음
def solution(s):
    if len(s)==1:
        return 0
    stack,index = [], 0
    while True:
        if s[index]==s[index+1]:
            index+=2
            if index>len(s)-1:
                break
        else:
            stack.pop() if s[index] in stack[-1:] else stack.append(s[index])
            index+=1
        if index==len(s)-1:
            stack.pop() if s[index] in stack[-1:] else stack.append(s[index])
            break
    return 1 if stack==[] else 0