# s	                    result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	                123

s='one4seveneight'

def solution(s):
    answer = ''
    alpha = ''
    eng_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if s.isdigit() == True: #숫자로만 이루어진 문자열이면 바로 return
        answer = s
    else:
        for i in s:
            if i.isdigit() == True: #숫자인 부분은 숫자를 문자열로 추가
                answer += i
            else: 
                alpha += i #문자열이 나오면 alpha 리스트에 모아놨다가
                if alpha in eng_num: #eng_num에 해당되면 index 뽑기, 그 인덱스가 그 숫자
                    num = eng_num.index(alpha)
                    answer += str(num)
                    alpha = ''

    return int(answer)

print(solution(s))