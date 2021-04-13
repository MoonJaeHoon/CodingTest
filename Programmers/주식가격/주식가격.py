from queue import deque
def solution(prices):
    answer, prices = [], deque(prices)
    while prices:
        current,time = prices.popleft(), 0
        for i in prices:
            if i>=current:
                time+=1
            else:
                time+=1
                break
        answer.append(time)
    return answer