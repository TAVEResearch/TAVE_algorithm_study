# date: 2021.11.18
# author: jeiyoon
def solution(a: int, b: int) -> str:
    # 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
    if month < 1 or month > 13:
        return -1
    
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    if month == 1:
        if date < 1 or date > 31:
            return 0
        result = day[(5+date-1)%7]
    elif month == 2:
        if date < 1 or date > 29:
            return 0
        result = day[(1+date-1)%7]
    elif month == 3:
        if date < 1 or date > 31:
            return 0
        result = day[(2+date-1)%7]
    elif month == 4:
        if date < 1 or date > 30:
            return 0
        result = day[(5+date-1)%7]
    elif month == 5:
        if date < 1 or date > 31:
            return 0
        result = day[(0+date-1)%7]
    elif month == 6:
        if date < 1 or date > 30:
            return 0
        result = day[(3+date-1)%7]
    elif month == 7:
        if date < 1 or date > 31:
            return 0
        result = day[(5+date-1)%7]
    elif month == 8:
        if date < 1 or date > 31:
            return 0
        result = day[(1+date-1)%7]
    elif month == 9:
        if date < 1 or date > 30:
            return 0
        result = day[(4+date-1)%7]
    elif month == 10:
        if date < 1 or date > 31:
            return 0
        result = day[(6+date-1)%7]
    elif month == 11:
        if date < 1 or date > 30:
            return 0
        result = day[(2+date-1)%7]
    else:
        if date < 1 or date > 31:
            return 0
        result = day[(4+date-1)%7]
        
    return result


a = 5
b = 24
print(solution(a, b))
