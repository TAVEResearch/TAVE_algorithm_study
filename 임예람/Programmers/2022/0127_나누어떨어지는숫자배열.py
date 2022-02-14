arr = [5, 9, 7, 10]
divisor = 5


def solution(arr, divisor):
    answer = []
    for num in arr:
        if (num % divisor) == 0:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer


print(solution(arr, divisor))
