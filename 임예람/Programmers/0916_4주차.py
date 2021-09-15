
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
    jobGrade = []

    for idx, langs in enumerate(table):
        eachGrade = [] #[0, 0, 0, 0, 14, 0] 이런식으로 직업군 수만큼 쌓임
        langsArr = langs.split(' ') #[SI, JAVA, JAVASCRIPT, SQL, PYTHON, C#]
        for lang in langsArr:
            for useLang in languages:
                if lang == useLang: #테이블 속 언어와 사용 언어가 같으면
                    #테이블의 각 언어가 받은 점수를 구한다
                    langGrade = langsArr.index(lang) 
                    if langGrade > 3: 
                        langGrade = 5 - langGrade + 1
                    elif langGrade < 3:
                        langGrade = 6 - langGrade
                    #언어별 선호도 총합을 구한다
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
    finalAnswer = []
    if len(maxGrade) == 1:
        answer = table[maxGrade[0]]
        job = answer.split(' ')
        answer = job[0]
    else:
        for idx, value in enumerate(maxGrade):
            answerList.append(table[maxGrade[idx]])
        for i in answerList:
            job = i.split(' ')
            finalAnswer.append(job[0])
        finalAnswer.sort()
        answer = finalAnswer[0]
    return answer

solution(table, languages, preference)