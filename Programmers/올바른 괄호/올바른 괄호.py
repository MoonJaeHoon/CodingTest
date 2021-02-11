def solution(s):
    left, right = 0, 0
    if not s.startswith('(') or not s.endswith(')'):
        return False
    for i in s:
        if i=='(':
            left+=1
        else:
            right+=1
        if left<right:
            return False
    return True if left==right else False