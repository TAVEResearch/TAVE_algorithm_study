def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)

    return answer


import collections


# 인규
def solution_i(p, c):
    p.sort()
    c.sort()
    result = collections.Counter(p) - collections.Counter(c)
    return list(result)[0]


part = ["leo", "kiki", "eden"]
compl = ["eden", "kiki"]
print(solution(part, compl))
