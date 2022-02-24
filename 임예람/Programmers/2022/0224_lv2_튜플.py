from collections import Counter

s= "{{1,2,3},{2,1},{1,2,4,3},{2}}"
def solution1(s):
    striped_s = s.strip("{""}")                     #2},{2,1},{2,1,3},{2,1,3,4
    s_list = striped_s.split("},{")                 #['2', '2,1', '2,1,3', '2,1,3,4']
    long_s = max( s_list, key = lambda x : len(x))  #2,1,3,4
    answer = [ int(i) for i in long_s if i != ","]  #['2', '1', '3', '4']
    return answer


def solution2(s):
    striped_s = s.strip("{""}")  
    s_list = [ list.split(',') for list in striped_s.split("},{")]    #[['1', '2', '3'], ['2', '1'], ['1', '2', '4', '3'], ['2']]     
    s_dic = {}
    for element in s_list:
        for num in element:  
            if num not in s_dic.keys():
                s_dic[num] = 1
            else:
                s_dic[num] += 1
    answer = Counter(s_dic).most_common()
    return [ int(i[0]) for i in answer]