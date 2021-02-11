def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]


'''
처음 풀이하는데 있어서 Enter에 대해 먼저 dict를 만들고 Change에 대해 dict를 만들어서 에러가 발생
다음 반례를 생각해보길,
1.prodo 입장 ->
2.prodo에서 ryan으로 Change ->
3.prodo 퇴장 ->
4.prodo로 재입장

return ['prodo 입장','prodo 퇴장','prodo 입장']

Change가 최종적인 닉네임이 아님,,
재입장시에도 닉네임변경이 가능하다는 것을 배제하고 풀어서 틀린 것.
'''
'''
comprehension은 가독성이 너무 떨어지기 때문에...

def solution(record):
    
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    
    answer = []
    
    for E_L in record:
        if E_L.startswith('Enter'):
            answer.append(f'{user_id[E_L.split()[1]]}님이 들어왔습니다.')
        elif E_L.startswith('Leave'):
            answer.append(f'{user_id[E_L.split()[1]]}님이 나갔습니다.')
    
    return answer
'''