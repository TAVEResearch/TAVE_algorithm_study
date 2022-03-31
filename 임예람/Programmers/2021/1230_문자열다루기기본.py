# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
s = "1234"
def solution(s):
    answer = False

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
    
    return answer

print(solution(s))


#다른 사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)