def transform_jinsu(n,origin_number):
    alphabet_dict = {k:v for k,v in zip(list(range(10,16)),['A','B','C','D','E','F'])}
    n_jinsu = ''
    while origin_number>=n:
        if origin_number%n<10:
            n_jinsu = str(origin_number%n) + n_jinsu
        else:
            n_jinsu = alphabet_dict[origin_number%n] + n_jinsu            
        origin_number //= n
    return str(origin_number) + n_jinsu if origin_number<10 else alphabet_dict[origin_number] + n_jinsu

def solution(n, t, m, p):
    answer = ''
    for origin_number in range(t*m+1):
        answer+=transform_jinsu(n,origin_number)
    return answer[p-1:t*m][::m]