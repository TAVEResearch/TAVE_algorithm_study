def solution(num: int) -> int:
    flag = 0
    count = 0
    
    for i in range(0,501):
        if i == 500:
            flag = -1
            break
        if num == 1:
            count = i
            break
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
    
    if flag == -1:
        return -1
    else:
        return count

n = 6
# n = 16
# n = 626331

print(solution(n))
