def solution(s: str):
    num_word = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    answer = ''
    word = ''
    for string in s:
        if string.isdigit():
            answer += string
        else:
            word += string
            if word in num_word.keys():
                answer += str(num_word[word])
                word = ''

    return int(answer)


if __name__ == '__main__':
    s = "one4seveneight"
    # num_word = {
    #     'zero': 0,
    #     'one': 1,
    #     'two': 2,
    #     'three': 3,
    #     'four': 4,
    #     'five': 5,
    #     'six': 6,
    #     'seven': 7,
    #     'eight': 8,
    #     'nine': 9
    # }
    # for i in num_word.keys():
    #     print(len(i))
    print(solution(s))
