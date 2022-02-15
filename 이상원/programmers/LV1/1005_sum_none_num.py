def solution(numbers):
    answer = 0
    for i in range(10):
        if i in numbers:
            continue
        else:
            answer += i
    return answer


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 6, 7, 8, 0]
    print(solution(numbers))
