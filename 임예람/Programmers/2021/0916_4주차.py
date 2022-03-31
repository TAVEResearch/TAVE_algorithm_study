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
    jobGrade = [] #ex) [29, 36, 41, 21, 25]
    jobName = [] #ex) ['SI', 'CONTENTS', 'HARDWARE', 'AHARDWARE', 'PORTAL', 'GAME']

    for idx, langs in enumerate(table):
        eachGrade = [] #[0, 0, 0, 0, 14, 0] 이런식으로 직업군 수만큼 쌓임
        langsArr = langs.split() #[SI, JAVA, JAVASCRIPT, SQL, PYTHON, C#]
        for lang in langsArr:
            #직업군 이름 저장
            if langs.index(lang) == 0:
                jobName.append(lang)
            print(jobName)
            #직업군별 언어별 선호도 계산
            for useLang in languages:
                if lang == useLang: #테이블 속 언어와 사용 언어가 같으면
                    #언어별 선호도 총합을 구한다
                    langGrade = 6 - langsArr.index(lang) 
                    eachGrade.append(langGrade * preference[languages.index(useLang)])
                else: #사용 언어가 없으면 선호도 0으로 처리
                    eachGrade.append(0) #[langsArr.index(lang)]
                
        # 각 직업군 idx에 선호도 총합을 기록 ex)[29, 36, 41, 21, 25]
        jobGrade.append(sum(eachGrade))
    
    # 최댓값인 직업군들의 idx 구하기 ex)[2]
    maxGrade = []
    for idx, value in enumerate(jobGrade):
        if value == max(jobGrade):
            maxGrade.append(idx)
    
    #직업군 이름 추출
    answerList = []
    if len(maxGrade) == 1:
        answer = jobName[maxGrade[0]]
    else:
        for idx, value in enumerate(maxGrade):
            answerList.append(jobName[maxGrade[idx]])
        answerList.sort()
        answer = answerList[0]
    return answer

print(solution(table, languages, preference))