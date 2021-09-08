def solution(price, money, count):

    result = 0
    total_price = 0
    
    #놀이기구를 몇 번 탔느냐에 따른 총 이용료
    for i in range(1, count + 1):
        total_price += price * i
    
    
    #가진 돈과 가격을 비교해서 결과를 출력
    if money < total_price:
        result = total_price - money
    else: 
        result = 0

    return result