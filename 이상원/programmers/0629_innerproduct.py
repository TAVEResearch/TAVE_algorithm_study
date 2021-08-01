def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j

    return answer


a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
print(solution(a, b))
