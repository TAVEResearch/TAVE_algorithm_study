"""
n이 주어지면 n의 각 자릿수의 합을 구해 리턴 

"""


def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer


if __name__ == "__main__":
    print(solution(123))
