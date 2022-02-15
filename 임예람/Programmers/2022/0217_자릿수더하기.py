def solution(n):
    numberList = list(map(int, str(n)))
    answer = sum(numberList)

    return answer

print(solution(123))