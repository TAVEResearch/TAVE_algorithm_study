def solution(s):
    length = len(s)
    half = length // 2

    if length % 2 == 0:
        return s[half - 1:half + 1]
    else:
        return s[half:half + 1]


if __name__ == '__main__':
    s = 'qwer'
    print(solution(s))
