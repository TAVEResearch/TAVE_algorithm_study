# 체육복

def solution(n, lost, reserve):
    answer = 0
    std = [1] * n  # 사람 수 만큼 1로된 배열 생성
    for i in lost:
        std[i - 1] -= 1  # 잃어버린 학생들 체육복 갯수 -1 해주기
    for i in reserve:
        std[i - 1] += 1  # 여벌있는 학생들 체육복 수 +1
    for i in range(len(std)):
        if std[i] == 2:  # 학생 리스트에 체육복 수 2개일 경우
            if i > 0 and std[i - 1] == 0:  # 앞 번호 학생이 있고 앞 학생의 옷이 0개면
                std[i] -= 1  # 옷 제공해 주는 학생 옷 수 -1
                std[i - 1] += 1  # 없는 학생 옷 개수 +1
            elif i < len(std) - 1 and std[i + 1] == 0:  # 뒷 번호 학생이 있고 뒷번호 학생 옷 0개면
                std[i] -= 1
                std[i + 1] += 1  # 뒷 번호 학생 옷 개수 +1
    for i in std:
        if i != 0:
            answer += 1  # 옷 개수 0이 아니면 +1로 학생 수 카운트
    return answer


if __name__ == '__main__':
    # 테스트 케이스
    n = 7
    lost = [1, 2, 3, 6]
    reserve = [1, 4]
    print(solution(n, lost, reserve))
