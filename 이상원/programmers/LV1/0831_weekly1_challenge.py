def solution(price, money, count):
    _money = 0
    for i in range(1, count + 1):
        _money += price * i

    if _money > money:
        return _money - money
    else:
        return 0


if __name__ == '__main__':
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))
