#s="abcde" #"c"
s="qwer"  #"we"


def solution(s):
    answer = ''
    length = divmod(len(s), 2)
    #(2, 1) 몫, 나머지

    if length[1] == 0: #길이 짝수
        answer = s[length[0]-1] + s[length[0]]
    else: #길이 홀수
        answer = s[length[0]]

    return answer

solution(s)