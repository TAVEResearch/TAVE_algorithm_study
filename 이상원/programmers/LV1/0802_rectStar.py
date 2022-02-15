def sol(input_str: str):
    a, b = map(int, input_str.strip().split(' '))
    star = '*' * (a * b)
    for line in range(1, len(star) + 1):
        if line % a == 0:
            print(star[line - a:line])


if __name__ == '__main__':
    sol('5 3')
