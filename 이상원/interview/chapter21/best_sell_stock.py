def best_sell_stock(day: list):
    result = 0
    # 값을 모르는 경우 매번 그리디 계산
    # 모두 비교해서 연산
    for i in range(len(day) - 1):
        if day[i + 1] > day[i]:
            result += day[i + 1] - day[i]

    return result


def maxProfit(price: list) -> int:
    # 0보다 크면 무조건 합산
    return sum(max(price[i + 1] - price[i], 0) for i in range(len(price) - 1))


if __name__ == '__main__':
    price = [7, 1, 5, 3, 6, 4]
    print(best_sell_stock(price))
    print(maxProfit(price))
