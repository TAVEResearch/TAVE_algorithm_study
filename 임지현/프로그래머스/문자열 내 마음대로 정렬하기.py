def solution(strings, n):
    strings = sorted(strings)

    for i in range(len(strings)):
        idx=i
        for j in range(i, len(strings)):
            if strings[idx][n] > strings[j][n]:
                idx=j
        strings[idx], strings[i]= strings[i], strings[idx]
        strings[i+1:] = sorted(strings[i+1:])
    return strings
