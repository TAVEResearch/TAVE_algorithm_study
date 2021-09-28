def solution(s):
    answer = ""
    try:
        return int(s)
    except:
        dic = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"      
        }
        num = ""
        for i in s:
            num += i
            try:
                if int(num):
                    answer += num
                    num = ""
            except:
                if num in dic:
                    answer += dic[num]
                    num = ""
        return int(answer)



s = "23four5six7"
print(solution(s))





