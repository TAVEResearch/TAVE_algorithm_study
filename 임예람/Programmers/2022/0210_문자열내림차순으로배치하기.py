s = "Zbcdefg"	

def solution(s):
    answer = ''
    capitalLetter = []
    smallLetter = []
    for letter in sorted(s, reverse=True):
        if letter.isupper():
            capitalLetter.append(letter)
        else:
            smallLetter.append(letter)
    answer = ''.join(smallLetter) + ''.join(capitalLetter)
    return answer

print(solution(s))


#다른 사람 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))