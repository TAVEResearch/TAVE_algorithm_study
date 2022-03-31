# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
s='a B z'
n=4

capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if s[i] in capital:
            after_idx = capital.index(s[i]) + n
            if after_idx > 25:
                after_idx = after_idx - 26
            answer += capital[after_idx]
        elif s[i] in lower:
            after_idx = lower.index(s[i]) + n
            if after_idx > 25:
                after_idx = after_idx - 26
            answer += lower[after_idx]
        else: #공백
            answer += " "

    return answer

#다른 사람 풀이
def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)



print(solution2(s,n))