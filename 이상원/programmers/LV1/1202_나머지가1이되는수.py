def solution(n):
    answer = 0
    _findForN = n - 1  # n보다 1 작은 수의 약수를 찾아야한다
    findForN = _findForN // 2  # 절반을 나눠 가장 작은 약수를 찾는다
    for num in range(2, _findForN + 1):
        if _findForN % num == 0:
            answer = num
            break
    return answer


if __name__ == '__main__':
    n = [10, 12]
    for i in n:
        print(solution(i))
