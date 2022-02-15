import collections


def solution(table: list, languages: list, preference: list):
    answer = ''
    _table = []
    for i in table:
        split_str = i.split(' ')
        _table.append(split_str[::-1])

    score = {'SI': 0, 'CONTENTS': 0, 'HARDWARE': 0, 'PORTAL': 0, 'GAME': 0}

    for work in _table:
        for _lang, _pref in zip(languages, preference):
            if _lang in work:
                lang_score = work.index(_lang) + 1
                score[work[-1]] += lang_score * _pref
    _max = [k for k, v in score.items() if max(score.values()) == v]

    return sorted(_max)[0]


if __name__ == '__main__':
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
             "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
             "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    lang = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    print(solution(table, lang, preference))
