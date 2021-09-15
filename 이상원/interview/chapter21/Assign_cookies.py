import bisect


def findCounter(g: list, s: list) -> int:
    # EX: g: grid factor
    # EX: s: 쿠키 개수??
    g.sort()
    s.sort()

    child_i = cookies_j = 0
    # 만족하지 못 할때까지 그리디 진행
    while child_i < len(g) and cookies_j < len(s):
        if s[cookies_j] >= g[child_i]:
            child_i += 1
        cookies_j += 1

    return child_i


def BST(g: list, s: list):
    g.sort()
    s.sort()

    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result


if __name__ == '__main__':
    cookies = [1, 2, 3]
    cookies1 = [1, 1]
    print(BST(cookies, cookies1))
