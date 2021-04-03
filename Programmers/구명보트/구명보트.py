def solution(people, limit):
    people.sort()
    answer, a, b = len(people), 0, len(people)-1
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1
            answer-=1
        b-=1
    return answer