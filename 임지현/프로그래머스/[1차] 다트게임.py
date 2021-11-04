

def solution(dartResult):
    answer = 0
    new_list = []
    first, second, third = -1,-1,-1  # 숫자 인덱스 위치 저장
    flag = 0

    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
          flag = 1
          continue
        elif flag and dartResult[i].isdigit():
            new_list.append(dartResult[i-1] + dartResult[i])
            flag = 0
        else:
          new_list.append(dartResult[i])

    for idx,char in enumerate(new_list):
        if char.isdigit():
            if first < 0:
                first = idx
            elif second < 0:
                second = idx
            else:
                third = idx
        elif char.isalpha():
            if char == 'S':
              continue;
            elif char == 'D':
                new_list[idx-1] = int(new_list[idx-1])**2
            else:
                new_list[idx-1] = int(new_list[idx-1])**3
        else:
            if char == '*':
                if third < 0:
                    new_list[first] = int(new_list[first]) * 2
                    if second > 0:
                        new_list[second] = int(new_list[second]) * 2
                else:
                    new_list[second] = int(new_list[second]) * 2
                    new_list[third] = int(new_list[third]) * 2
            else:
                new_list[idx-2] = int(new_list[idx-2]) * (-1)

    answer = int(new_list[first]) + int(new_list[second]) + int(new_list[third])      

    
    return answer
  
  
  
