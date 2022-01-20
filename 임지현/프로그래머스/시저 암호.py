def solution(s, n):
    answer = ''
    for char in s:
        # char가 공백일 경우
        if char == " ":
            answer += " "
            continue
        digit = ord(char)
        digit += n
        if char.isupper() and digit > 90:
            r = digit % 90
            digit = 64 + r
        elif char.islower() and digit > 122:
            r = digit % 122
            digit = 96 + r
        answer += chr(digit)
        
    return answer
