def solution(s):
    s = s.lower()
    p_cnt = s.count('p')
    y_cnt = s.count('y')
    
    if p_cnt == y_cnt:
        return True
    else:
        return False
