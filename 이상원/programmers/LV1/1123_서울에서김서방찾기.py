def solution(seoul):
    idx = seoul.index("Kim")
    return f'김서방은 {idx}에 있다'


if __name__ == '__main__':
    seoul = ["Jane", "Kim"]
    print(solution(seoul))
