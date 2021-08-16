def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr


if __name__ == '__main__':
    arr = [4, 3, 2, 1]
    print(solution(arr))
