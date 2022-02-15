def solution(n):
    answer = ''
    pattern = '수박'
    mul = n // len(pattern)
    remain = n % len(pattern)
    for i in range(mul):
        answer += pattern
    if remain == 0:
        return answer
    else:
        answer += pattern[0]
        return answer


if __name__ == '__main__':
    n = 3
    print(solution(n))
