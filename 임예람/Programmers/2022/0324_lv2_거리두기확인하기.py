places = [ ["POOOP", 
            "OXXOX", 
            "OPXPX", 
            "OOXOX", 
            "POXXP"]]
            # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            # ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
            # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

#for 돌리다가 x면 0으록 하고 p면 2, o면 1을 더해보자?
#첫줄을 돌린다. 옆을 확인, 뒷줄 확인

def checkSomethingInRow(object):
    try:
        object.isdigit()
        if object == 'P':
            return 2
        elif object == 'O':
            return 1
        elif object == 'X':
            return 0
    except AttributeError:
        pass

d = [[],[],[],[],[]]

def solution(places):
    answer = []
    for room_idx, room in enumerate(places): # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
        for row_idx, row in enumerate(room): #"POOPX"
            row_list = [] #21120
            for obj_idx, object in enumerate(row):   #P
                if object == 'P':
                    row_list.append(2)
                elif object == 'O':
                    row_list.append(1)
                else: 
                    row_list.append(0)

                if obj_idx == 1:
                    pass
                elif (row_list[obj_idx] + row_list[obj_idx - 1]) > 4:
                    answer.append(0)
                    break
                    
            # room[row_idx] = list(row)
            # print(places)
            # for object_idx in range(len(room[row_idx])):
                # pass
                # print('hi',row)
            #     if object_idx == 4: #맨 끝자리면 다음 사람 못 봄
            #         row[object_idx] = checkSomethingInRow(row[object_idx])
            #         pass
            #     else:
            #         print(row[object_idx])
            #         row.replace()
            #         row[object_idx] = checkSomethingInRow(row[object_idx]) #2
            #         row[object_idx + 1] = checkSomethingInRow(row[object_idx])
            #         print('this is -----',row[object_idx], row[object_idx + 1])
                
                # pass
            # if "POP" in row or "PP" in row: #한 줄에 붙어있나 check
            #     answer.append(0) 
            #     break
            # elif row >= 1 and row <= 3: #2,3,4줄일 때
            #     for col in row:
            #         pass
    # return places   


# print(solution(places))

#각 함수에 따라 숫자를 출력하는 함수를 만들어보자
idx = ['X', 'O', 'P']

def returnNum(alphbet):
    if alphbet == 'X':
        return 0
    elif alphbet == 'O':
        return 1
    else:
        return 2

def solution(places):
    pass