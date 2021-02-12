def solution(n, words):
    before = [words[0]]
    for index in range(1,len(words)):
        if (not words[index].startswith(before[-1][-1]) ) or (words[index] in before):
            return [index%n+1,index//n+1]
        before.append(words[index])
    return [0,0]