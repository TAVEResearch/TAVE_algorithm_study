# 신규 아이디 추천

import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-zA-Z0-9_.-]", "", new_id)

    while ".." in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id[1:] if new_id[0] == '.' and len(new_id) > 1 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id

    if len(new_id) == 0:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id[0] == "." and new_id[1:] or new_id
        new_id = new_id[-1] == "." and new_id[:-1] or new_id
    if len(new_id) <= 3:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id

    return answer


inp = "=.="
print(solution(inp))
