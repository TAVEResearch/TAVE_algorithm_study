def solution(sizes):
    verticalMax = 0
    horizontalMax = 0

    for i in sizes:
        ISort = sorted(i)
        if verticalMax < ISort[0]:
            verticalMax = ISort[0]
        if horizontalMax < ISort[1]:
            horizontalMax = ISort[1]

    return horizontalMax * verticalMax


if __name__ == '__main__':
    size = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(size))
