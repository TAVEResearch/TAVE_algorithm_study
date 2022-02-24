"""
https://programmers.co.kr/learn/courses/30/lessons/64065
중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
튜플의 원소 개수는 유한합니다.

중복 원소가 없는 튜플이 있을 때 
"""

import collections


def watchOne(getStr, dictStr):
    forStr = getStr[:-2].split(",")
    for item in forStr:
        dictStr[item] += 1
    return dictStr


def solution(s: str):
    sSplit = s.split("{")
    remNone = list(filter(None, sSplit))
    strDict = collections.defaultdict(int)

    for i in remNone:
        strDict = watchOne(i, strDict)

    answer = sorted(strDict.items(), key=lambda x: x[1], reverse=True)
    lst = []
    for i in answer:
        lst.append(int(i[0]))
    return lst


s = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]

for i in s:
    print(solution(i))
