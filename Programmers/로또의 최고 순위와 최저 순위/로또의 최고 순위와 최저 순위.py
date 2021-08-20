def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    overlaps = sum([lot in win_nums for lot in lottos])
    high = 7-(overlaps+zero_count) if overlaps+zero_count>=2 else 6
    low = 7-overlaps if overlaps>=2 else 6
    answer = [high,low]
    return answer
