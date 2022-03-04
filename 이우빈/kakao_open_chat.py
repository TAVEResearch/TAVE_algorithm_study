from typing import List

def solution(record: List[str]) -> List[str]:  
    answer = []
    userDB = dict()
    actions = []

    for event in record:
        info = event.split() # record -> [action, userid, nickname]
        action, userid = info[0], info[1]

        if action in ('Enter', 'Change'):
            nickname = info[2]
            userDB[userid] = nickname

        actions.append([userid, action])


    for actionInfo in actions:
        userid, action = actionInfo[0], actionInfo[1]
        
        if action == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(userDB[userid])) # answer.append(f'{userDB[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(userDB[userid]))

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))