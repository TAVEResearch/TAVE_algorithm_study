def solution(a, b):
    '''
    a, b 사이에 속한 모든 정수의 합을 리턴
    :param a: 정수
    :param b: 정수
    :return: 정수의 합
    '''
    answer = 0

    if a == b:
        answer = a
    else:
        for i in range(min(a, b), max(a, b) + 1):
            answer += i

    return answer


if __name__ == '__main__':
    a = [3, 3, 5]
    b = [5, 3, 3]
    for _a, _b in zip(a, b):
        print(solution(_a, _b))
