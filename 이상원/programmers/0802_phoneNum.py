def solution(phone_number: str):
    answer = ''
    answer += '*' * (len(phone_number) - 4)
    answer += phone_number[-4:]

    return answer


if __name__ == '__main__':
    print(solution("01033334444"))
