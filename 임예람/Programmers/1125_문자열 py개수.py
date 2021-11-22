s="pPoooyY"	
# true
ss="Pyy"	
# false

def solution(s):
    answer = True

    s = s.lower()
    countP = s.count('p')
    countY = s.count('y')

    if 'p' not in s and 'y' not in s:
        return answer
    elif countP == countY:
        answer = True
    else:
        return False

    return answer