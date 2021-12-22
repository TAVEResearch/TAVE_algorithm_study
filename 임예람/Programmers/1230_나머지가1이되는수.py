#자연수 n이 매개변수로 주어집니다. 
#n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

n=10 #3
n2=12 #11

def solution(n):
    for i in range(n):
        last = n % (i+1)
        if last == 1:
            return i+1

solution(n)