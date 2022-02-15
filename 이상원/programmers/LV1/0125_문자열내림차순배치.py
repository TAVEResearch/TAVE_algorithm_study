def solution(s):
    '''
    문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴
    :param s: 문자열 s
    :return: 문자열
    '''
    answer = ''
    sSort = ''.join(sorted(s, reverse=True))
    return sSort


if __name__ == '__main__':
    s = 'Zbcdefg'
    print(solution(s))
