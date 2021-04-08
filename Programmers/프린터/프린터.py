def solution(priorities, location):
    priorities_index = [i for i,j in enumerate(priorities)]
    printed = []
    printed_index = []
    
    while len(priorities)>0:
        get = priorities.pop(0)
        get_index = priorities_index.pop(0)
        if len(priorities)==0:
            printed.append(get)
            printed_index.append(get_index)            
        elif get < max(priorities):
            priorities.append(get)
            priorities_index.append(get_index)
        else:
            printed.append(get)
            printed_index.append(get_index)
            
    answer = printed_index.index(location)+1
    return answer