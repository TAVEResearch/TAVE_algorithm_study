def getMonth(getA):
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    days = 0

    if getA in thirtyOne:
        days += 31
    elif getA in thirty:
        days += 30
    elif getA == 2:
        days += 29
    return days


def solution(a, b):
    answer = ''
    day = {2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU', 0: 'FRI', 1: 'SAT'}
    days = 0
    for month in range(1, a):
        days += getMonth(month)
    days += b - 1
    outDay = days % 7

    return day[outDay]


if __name__ == '__main__':
    # 윤년 2월 29일 -> 366일
    # 1월 1일 금요일
    a = 5
    b = 24
    print(solution(a, b))
