def solution_timeout(n):
    answer = 0
    sam = ''
    div = 1
    while div > 0:
        div, remain = n // 3, n % 3
        n = div
        sam += str(remain)

    multiple = len(sam) - 1
    for _iter in range(len(sam)):
        answer += (3 ** multiple) * int(sam[_iter])
        multiple -= 1
    return answer


def solution_timeout_(n):
    # fixme 시간 초과
    answer = 0
    sam = ''
    while True:
        div, remain = divmod(n, 3)
        n = div
        sam += str(remain)
        if div == 1:
            sam += str(div)
            break
    print(sam)
    samReverse = sam[::-1]
    print(samReverse)
    multiple = 3
    for num in range(1, len(samReverse) + 1):
        if num == 1:
            answer += int(samReverse[num - 1]) * num
        else:
            answer += int(samReverse[num - 1]) * multiple
            multiple *= 3
    return answer


def solution(n):
    answer = 0
    numList = []
    while True:
        div, remain = n // 3, n % 3
        n = div
        numList.insert(0, remain)
        if div == 1:
            numList.insert(0, div)
            break

    multiple = 3
    for num in range(1, len(numList) + 1):
        if num == 1:
            answer += numList[num - 1] * num
        else:
            answer += numList[num - 1] * multiple
            multiple *= 3
    return answer


if __name__ == '__main__':
    n = [45, 125]
    for i in n:
        print(solution_timeout_(i))
