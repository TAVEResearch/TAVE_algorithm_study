new_id = "...!@BaT#*..y.abcdefghijklm..."
#"bat.y.abcdefghi"

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

def solution(new_id):
    answer = ''
    step1 = new_id.lower()

    special_letter = "" #!@#*
    for i in step1:
        if not i.isalnum() and not i.isdigit() and i != "-" and i != "_" and i != ".":
            special_letter += i
    step2 = ''.join(x for x in step1 if x not in special_letter) #...bat..y.abcdefghijklm

    step3 = "" #.bat.y.abcdefghijklm
    dots = ""
    for i in step2: #마지막이 마침표면 빠지게 되는데 차피 3단계에서 제거할거니까 걍 넘어가기~
        if i != ".": #마침표 아니면 그냥 더하기
            if len(dots) > 0: #마침표 1개 이상 모이면 하나만 넣어주고 비우기
                step3 += '.'
                dots=""
            step3 += i
        else: #마침표면 모아두기
            dots += i

    #양쪽 마침표 제거
    step4 = step3.strip('.') #bat.y.abcdefghijklm

    step5 = "" #bat.y.abcdefghijklm
    if step4 == "":
        step5 += 'a'
    else:
        step5 += step4

    step6 = "" #bat.y.abcdefghij
    if len(step5) > 15:
        step6 += step5[0:15].rstrip('.')
    else:
        step6 += step5
    
    step7 = ""
    if len(step6) < 3:
        step7 += step6
        for i in range(3-len(step6)):
            step7 += step6[-1]
    else:
        step7 += step6

    return step7

print(solution(new_id))