def is_prime_number(x):
    num = 0
    for i in range(1, x + 1):
        if x % i == 0:
            num += 1
    return num


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        isPrime = is_prime_number(i)
        if isPrime % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


if __name__ == '__main__':
    left = 13
    right = 17
    print(solution(left, right))
