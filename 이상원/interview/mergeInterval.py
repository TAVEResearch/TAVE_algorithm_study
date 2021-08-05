# p497
# No.59


def merge(intervals: list) -> list:
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            print(i, )
            # EX: i, 는 처음 봄
            # EX: i, 나 [i]로 사용 가능
            merged += i,
    return merged


if __name__ == '__main__':
    liInput = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(liInput))
