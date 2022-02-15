def solution(n):
    answer = 0
    half = n // 2
    lst = []
    for i in range(1, half + 1):
        if n % i == 0:
            lst.append(i)
    lst.append(n)
    answer = sum(lst)

    return answer


if __name__ == '__main__':
    n = [12, 5]
    for i in n:
        print(solution(i))
