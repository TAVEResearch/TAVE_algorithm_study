s = "try hello world"

def makeWeirdLetter(word):
    answer = ''
    for idx, letter in enumerate(word):
        if idx % 2 == 0:
            answer += letter.upper()
        else:
            answer += letter.lower()
    return answer


def solution(s):
    answer = ''
    sList = s.split(' ')

    for idx, word in enumerate(sList):
        if not idx == 0:
            answer += ' '
            answer += makeWeirdLetter(word)
        else:
            answer += makeWeirdLetter(word)
    return answer

print(solution(s))