def solution(lottos: list, win_nums: list) -> list:
    def rank(num: int) -> int:
        if num > 1:
            return 7 - num
        else:
            return 6

    low = 0
    high = 0
    for i in lottos:
        if i in win_nums:
            low += 1
        if i == 0:
            high += 1
    high += low

    return [rank(high), rank(low)]

    lotto = [44, 1, 0, 0, 31, 25]
    win_num = [31, 10, 45, 1, 6, 19]
    print(solution(lotto, win_num))
