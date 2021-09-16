# 입력값 〉	
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", #15+14=29
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", #21+10+5=36
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
        "AHARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
# 기댓값 〉	"HARDWARE"


def solution(table, languages, preference):
    answer = ''
    pref = dict(zip(languages, preference))
    result = []

    table = [col.split() for col in table]
    for column in table: #column=[GAME, C++, C#, JAVASCRIPT, C, JAVA]
        scores = []
        for n in range(1, len(column)): #인덱스 0인 직업군 제외하고 순회
            if column[n] in languages:
                scores.append((len(column)-n) * pref[column[n]])
        result.append((column[0], sum(scores)))

    answer = sorted(result, key=lambda x : (-x[1], x[0])) #1번 인덱스인 점수는 -를 붙여 내림차순, 0번 인덱스인 언어는 오름차순 정렬

    return answer

solution(table, languages, preference)