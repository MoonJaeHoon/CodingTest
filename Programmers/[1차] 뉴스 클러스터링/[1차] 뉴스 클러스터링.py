def solution(str1, str2):
    multi_str1 = [str1[ind:ind+2].lower() for ind in range(len(str1)-1) if str1[ind:ind+2].isalpha()]
    multi_str2 = [str2[ind:ind+2].lower() for ind in range(len(str2)-1) if str2[ind:ind+2].isalpha()]
    
    intersect = []
    for ms1 in multi_str1[:]:
        if ms1 in multi_str2:
            intersect.append(ms1)
            multi_str1.remove(ms1)
            multi_str2.remove(ms1)
    
    union = multi_str1+multi_str2+intersect
    return int(65536*len(intersect)/len(union)) if union!=[] else 65536