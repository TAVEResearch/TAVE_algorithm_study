def solution(n, arr1, arr2):
    answer = []

    def binary(x: str) -> str:
        while True:
            if len(x) == n:
                break
            x = '0' + x
        return x

    for i, j in zip(arr1, arr2):
        int_To_bin = bin(i | j)
        int_To_bin = binary(int_To_bin[2:])
        make_map = ""
        for b in int_To_bin:
            if b == "1":
                make_map += "#"
            else:
                make_map += " "
        answer.append(make_map)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
