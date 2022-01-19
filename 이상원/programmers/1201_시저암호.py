def getNextAscii(string):
    pass


def solution(s, n):
    '''
    각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식
    :param s: 문자열
    :param n: 거리
    :return: :type: str
    '''
    answer = ''
    '''
    a~z = 97 122
    A~Z = 65 90
    '''

    #  ord: 유니코드로 변환
    # chr() 유니코드를 문자로 변환
    lowerA = ord('a')
    lowerZ = ord('z')

    upperA = ord('A')
    upperZ = ord('Z')

    for alpha in s:
        newAlpha = ord(alpha) + n
        if alpha == ' ':
            answer += ' '
        elif alpha.islower() and newAlpha > lowerZ:
            newAlpha -= lowerZ + 1
            answer += chr(lowerA + newAlpha)
        elif alpha.isupper() and newAlpha > upperZ:
            newAlpha -= lowerZ + 1
            answer += chr(lowerA + newAlpha)
        else:
            answer += chr(newAlpha)

    return answer


if __name__ == '__main__':
    s = ["AB", "z", "a B z", "zzZZ"]
    n = [1, 1, 4, 2]
    for _s, _n in zip(s, n):
        print(solution(_s, _n))
