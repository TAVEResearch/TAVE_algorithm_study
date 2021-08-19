import collections


def solution(arr: list) -> int:
    res = 0
    for num in arr:
        res ^= num
    return res


if __name__ == '__main__':
    solution([2, 2, 1])
