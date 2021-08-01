# k번째 수
def solution(array, commands):
    answer = []
    for i in commands:
        x, y, z = i  # command 선언
        k_num = array[x - 1:y]  # 슬라이싱
        k_num.sort()  # sort
        answer.append(k_num[z - 1])  # 찾을 수 정답 배열에 넣기
    return answer


if __name__ == '__main__':
    arr = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(arr, commands))
