n=5

def solution(given_n):
    answer = 1 + given_n
    for devider in range(2, given_n): #1이랑 n 이미 더해서 2~n-1까지만
        if given_n % devider == 0:
            if devider == (given_n/devider) or devider > (given_n/devider):
                return answer
            else:
                answer += devider
                answer += (given_n / devider)
    return answer


print(solution(100))