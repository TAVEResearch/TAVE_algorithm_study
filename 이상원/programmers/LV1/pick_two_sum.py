# 두개 뽑아서 더하기

def solution(numbers):
    answer = []

    return answer


def solution_i(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer


# 동훈
from itertools import combinations


def solution_d(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))

    return sorted(answer)


inp = [2, 1, 3, 4, 1]

print(solution(inp))
