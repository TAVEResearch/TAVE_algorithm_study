def solution(arr, divisor):
    '''
    divisor로 나누어 떨어지는 값을 오름차순 정렬
    :param arr:
    :param divisor:
    :return:
    '''
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


if __name__ == '__main__':
    arr = [
        [5, 9, 7, 10],
        [2, 36, 1, 3],
        [3, 2, 6]
    ]
    divisor = [5, 1, 10]
    for ar, div in zip(arr, divisor):
        print(solution(ar, div))
