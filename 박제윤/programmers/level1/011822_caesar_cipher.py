# date: 2022.01.18
# author: jeiyoon
def solution(s: str, n: int) -> str:
    answer = ''
    overflow_coef = 26 # 90 - 65 + 1 or 122 - 97 + 1

    for char in s:
        # space -> add
        if char.isspace():
            answer += char
            continue

        # s consists of uppercase, lowercase, and space
        # assumption: Z -> A and z -> a
        # uppercase (A(65) - Z(90))
        if char.isupper():
            if ord(char) + n > ord("Z"):
                answer += chr(ord(char) - overflow_coef + n)
            else:
                answer += chr(ord(char) + n)
        # lowercase(a(97) - z(122))
        else:
            if ord(char) + n > ord("z"):
                answer += chr(ord(char) - overflow_coef + n)
            else:
                answer += chr(ord(char) + n)

    return answer

# result = "BC"
# s = "AB"
# n = 1

# result = "a"
# s = "z"
# n = 1

# result = "e F d"
s = "a B z"
n = 4

print(solution(s, n))
