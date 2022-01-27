def solution(arr):
    '''
    배열 arr 주어짐. 배열 숫자는 0~9 연속적으로 나타나는 숫자는 하나만 남기고 제거
    제거된 수 반환 시 arr의 원소들의 순서 유지
    arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
    :param arr: 0~9
    :return:
    '''
    answer = []
    for i in arr:
        answer.append(i)
        if len(answer) >= 2 and answer[-1] == answer[-2]:
            answer.pop()

    return answer


if __name__ == '__main__':
    arr = [
        [1, 1, 3, 3, 0, 1, 1],
        [4, 4, 4, 3, 3]
    ]
    for i in arr:
        print(solution(i))
