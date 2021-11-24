def solution(s):
    '''
    :param s: 주어진 문자열
    :return: bool -> num of p and y is same : return true
    '''
    pNum = 0
    yNum = 0
    for alpha in s:
        if alpha == 'p' or alpha == 'P':
            pNum += 1
        if alpha == 'y' or alpha == 'Y':
            yNum += 1

    return pNum == yNum


if __name__ == '__main__':
    s = ["pPoooyY", "Pyy"]
    for i in s:
        print(solution(i))
