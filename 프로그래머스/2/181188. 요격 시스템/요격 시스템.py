def solution(targets):
    
    targets.sort(key = lambda x:x[1])
    
    end, result = 0, 0
    
    for s, e in targets:
        if s >= end:
            result += 1
            end = e
    return result