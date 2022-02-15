def solution(strings, n):
    '''
    :param strings: 길이 1 이상 50이하 배열
    :param n: n번째 글자를 기준으로 오름차순
    :return: list
    각 문자열의 인덱스 n번째 글자를 기준으로 오름차순으로 정렬
    '''
    return sorted(strings, key=lambda x: (x[n], x))


if __name__ == '__main__':
    strings = [["sun", "bed", "car"],
               ["abce", "abcd", "cdx"]]
    n = [1, 2]
    for st, _n in zip(strings, n):
        print(solution(st, _n))
