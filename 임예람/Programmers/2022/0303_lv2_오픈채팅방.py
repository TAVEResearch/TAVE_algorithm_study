record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    member_list = {}
    for each_record in record:
        each_record_list = each_record.split(" ") #['Enter', 'uid1234', 'Muzi']

        #멤버 리스트를 만들어준다. ex) {'uid1234' : 'Muzi'}
        try:
            member_list[each_record_list[1]] = each_record_list[2]
        except IndexError:
            pass
        
        #누가 들어오고 나갔는지 기록을 남긴다.
        #ex) ['uid1234 들어왔습니다.', 'uid4567 들어왔습니다.', 'uid1234 나갔습니다.', 'uid1234 들어왔습니다.']
        if each_record_list[0] == "Enter":
            answer.append("{} 들어왔습니다.".format(each_record_list[1]))
        elif each_record_list[0] == "Leave":
            answer.append("{} 나갔습니다.".format(each_record_list[1]))
        else:
            pass
    
    for idx, management_record in enumerate(answer):
        management_record_list = management_record.split(" ")
        answer[idx] = answer[idx].replace(management_record_list[0], '{}님이'.format(member_list[management_record_list[0]]))

    return answer

print(solution(record))