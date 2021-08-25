## 1. 빅오 표기법 (Big O Notation)

- 0(1): 입력값이 아무리 커드 실행시간이 일정. 해시 테이블의 조회 및 삽입

- O(log n): 웬만한 n의 크기에 대해 매우 견고함. 이진 검색

- O(n): 선형 시간 (Linear-Time) 알고리즘. 모든 입력값을 적어도 한번이상 살펴봐야함. 정렬되지 않은 리스트에서 최댓값 또는 최솟값

- O(nlog n): 대부분 효율 좋은 정렬 알고리즘. 팀소트(Timsort)는 O(n)

- O(n^2): 비효율적. 버블정렬

- O(2^n): 피보나치 수를 재귀로 계산하는 알고리즘. n^2보다 훨씬 큼

- O(n!): 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제(Traveling Salesman Problem)
 


## 2. 상한과 최악

- 빅오(O)는 수행시간의 상한(Upper Bound)을 의미

- 하한은 빅오메가(Ω), 평균은 빅세타(Θ)


## 3. 분할상환분석 (Amortized Analysis, p106)

- 별로 중요한 것 같지 않으니 가끔씩 볼것


## 4. 임의정밀도 (p109)

- 정수를 숫자의 배열로 간주하여 무제한 자릿수를 제공하는 정수형

- 계산 속도가 저하됨. 오버플로를 고민할 필요가 없음. 즉, 기능과 안전을 위해 속도를 어느정도 포기한셈


## 5. 집합

```
a = set()
print(a)
```

- 빈 집합이 아닌 값이 포함된 집합을 선언할 때는 a = {1, 2, 3} 형태로 하는데, 집합은 딕셔너리와 동일하게 중괄호를 상요하므로 주의해야함

```
a = {'a', 'b', 'c'}
print(type(a)) # set

a = {'a':'A', 'b':'B', 'c':'C'}
print(type(a)) # dict

a = {'a', 'b', 'c', 'c', 'c'}
print(a) # {'a', 'b', 'c'}
```


## 6. 시퀀스 (Sequence)

- 불변: str, tuple, bytes
- 가변: list

```
a = 'abc'
print(id('abc')) # 4317530408
print(id(a)) # 4317530408

a = 'def'
print(id('def')) # 4318831648
print(id(a)) # 4318831648

a[1] = 'd' # TypeError: 'str' object does not support item assignment
```


## 7. 객체

- 파이썬은 모든게 객체

- 불변객체 (Immutable Object): bool, int, float, tuple, str

- 가변객체 (Mutable Object): list, set, dict

```
a = 10
b = a
print(id(10), id(a), id(b)) # same
```

```
a = [1, 2, 3, 4, 5]
b = a
print(b)
a[2] = 4
print(a)
print(b)
```

- 주의: b에 새로운 값을 할당하게 되면 더이상 b 변수는 a 변수를 참조하지 않음.

- 즉, 이제 b 변수는 7이라는 새로운 객체를 참조하게 됨

```
a = 10
b = a
print(id(a), id(b)) # same

b = 7
print(a, id(a), id(b)) # differenct
```


## 8. is 와 ==

- is 는 id를 비교

- == 는 값을 비교

- copy.deepcopy()로 복사한 결과 또한 값은 같지만 ID가 다름. 그래서 ==는 True, is는 False

```
a = [1, 2, 3]
a == copy.deepcopy(a) # True

a is copy.deepcopy(a) # False
```
