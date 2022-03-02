import collections


def solution(record):
    # > 사용자의 id를 기준으로 값을 갱신할 dict 생성
    usrId = collections.defaultdict()
    # > log를 돌면서 사용자 id가 변경되는 것 확인
    for i in record:
        info = i.split()
        if len(info) == 3:
            usrId[info[1]] = info[2]

    answer = []
    # > log를 돌면서 동작 state를 확인해서 위에서 정의한 사용자 dict에서 id를 기준으로 정답 배열 생성
    for i in record:
        usrInfo = i.split(" ")
        if usrInfo[0] == "Enter":
            answer.append(f"{usrId[usrInfo[1]]}님이 들어왔습니다.")
        elif usrInfo[0] == "Leave":
            answer.append(f"{usrId[usrInfo[1]]}님이 나갔습니다.")
        elif usrInfo[0] == "Change":
            continue
    return answer


# >state를 dict로 해서 푸는 방법도 괜찮을거 같다는 생각


if __name__ == "__main__":
    record = [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
    print(solution(record))
