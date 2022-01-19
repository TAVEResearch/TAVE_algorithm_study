def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdecimal()
    else:
        return False


if __name__ == '__main__':
    s = ["a234", "1234"]
    for i in s:
        print(solution(i))
