import re


def solution(dartResult):
    bonus_n_option = {'S': 1, 'D': 2, 'T': 3, '#': -1, '*': 2}
    sumOut = []
    out_lst = []
    num = ''
    numInt = 0
    for idx in dartResult:
        if idx.isnumeric():
            num += idx
            continue
        elif idx in 'SDT':
            sumOut.append(num)
            num = ''
            if sumOut[-1] == '':
                continue
            else:
                numInt = int(sumOut[-1]) ** bonus_n_option[idx]
                out_lst.append(numInt)
        elif idx == '#':
            out_lst[-1] = out_lst[-1] * bonus_n_option[idx]
        elif idx == '*':
            out_lst[-1] = out_lst[-1] * bonus_n_option[idx]
            if len(out_lst) >= 2:
                out_lst[-2] = out_lst[-2] * bonus_n_option[idx]
    return sum(out_lst)


if __name__ == '__main__':
    dartResult = '1S*2T*3S'
    print(solution(dartResult))
