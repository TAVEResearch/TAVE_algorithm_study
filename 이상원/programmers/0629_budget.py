def solution(d, budget):
    answer = 0
    while True:
        if len(d) == 0:
            break
        budget -= min(d)
        if budget < 0:
            break
        answer += 1
        d.remove(min(d))
    return answer


d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))
