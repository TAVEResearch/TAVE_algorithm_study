seoul = ["Jane", "Kim"]	
# output = "김서방은 1에 있다"

def solution(seoul):
    answer = 0

    answer += seoul.index("Kim")

    return "김서방은 {}에 있다".format(answer)

print(solution(seoul))