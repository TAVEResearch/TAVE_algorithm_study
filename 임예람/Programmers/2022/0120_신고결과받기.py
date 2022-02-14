from unittest import result


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k=2
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
result = [2,1,1,0]

def solution(id_list, report, k):
    #[id, 신고한 아이디 리스트, 신고 받은 횟수]
    answer = [] #answer :  [['muzi'], ['frodo'], ['apeach'], ['neo']]

    for idx, person in enumerate(id_list):
        answer.append([person, [], 0]) 

    for i in report:
        give_report, get_report = i.split(' ')[0], i.split(' ')[1]

        for id_idx, id in enumerate(id_list):
            if id == give_report: 
                #무지가 어떤 사람 신고했는지 얼마나 신고 받았는지 리스트로 저장
                if id_list.index(get_report) not in answer[id_idx][1]: #같은 사람 신고 제외
                    answer[id_idx][1].append(id_list.index(get_report))
                    answer[id_list.index(get_report)][2] += 1
                    print(answer)
    # answer
    # [['muzi', [1, 3], 1], 
    #   ['frodo', [3], 2], 
    #   ['apeach', [1, 0], 0], 
    #   ['neo', [], 2]]

    delete_list = [] #[1, 3]
    for id in answer:
        if id[2] >= k:
            delete_list.append(answer.index(id))
    
    mail_count = []
    for id in answer:
        mail = [i for i in set(id[1]).intersection(delete_list)] #[{1, 3}]
        print(mail)
        mail_count.append(len(mail))

    return mail_count

solution(id_list, report, k)