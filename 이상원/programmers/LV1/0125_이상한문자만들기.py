def newWord(word):
    words = ''
    # 같은 문자인 경우 hello 같은 경우
    # list.index를 쓰면 index값 잘못 가져온다
    for i in range(len(word)):
        if i % 2 == 0:
            words += word[i].upper()
        else:
            words += word[i].lower()
    return words


def solution(s):
    answer = ''
    sSplit = s.split(' ')
    for i in sSplit:
        answer += newWord(i)
        answer += ' '

    return answer[:-1]


if __name__ == '__main__':
    s = "Hello eVeryone"
    print(solution(s))
