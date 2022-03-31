left=13
right=17
#43


def solution(left, right):
    answer = 0

    for num1 in range(left, right+1):
        count = 0
        for num2 in range(1, num1+1):
            if num1 % num2 == 0: #나머지가 0이면 나뉘는 겨
                count += 1 
        print(num1, count)
        if count % 2 == 0: #2로 나뉘면 짝수
            answer += num1  
        else:
            answer -= num1

    return answer

print(solution(left, right))


# 다른사람 답 - 제곱수는 약수의 개수가 홀수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer