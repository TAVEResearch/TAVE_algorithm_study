## 1. 파이썬

- 파이썬은 어설프게 알고 있으면 안됨

- e.g.) 딕셔너리의 입력순서가 항상 유지된다? No

- 인덴트 (indent)는 공백 4칸을 원칙으로 함

```
foo = long_function_name(var_one, var_two,
	var_three, var_four)
```

- 위 코드처럼 첫 번째 줄에 파라미터가 있다면, 파라미터가 시작되는 부분에 보기 좋게 맞춤

```
def long_function_name(
	var_one, var_two, var_three,
	var_four):
	print(var_one)
```

- 위 코드에서처럼 첫 번째 줄에 파라미터가 없다면, 공백 4칸 인덴트를 한 번 더 추가하여 다른행과 구분되게 함

```
foo = long_function_name(
	var_one, var_two,
	var_three, var_four)
```

- 위 코드에서처럼 여러 줄로 나눠쓸 경우 다음 행과 구분되도록 인덴트를 추가함

- 근데 이런거 외울 필요 없이 그냥 파이참 쓰면 알아서 맞춰줌


## 2. 네이밍 컨벤션 (Naming Comvention)

- 변수명 네이밍 컨벤션은 스네이크 케이스 (Snake Case)를 따름

- 함수명도 마찬가지


## 3. 타입 힌트

- e.g.) a: str = "1"

- 온라인 코딩 테스트 시에는 mypy를 사용하면 타입 힌트에 오류가 없는지 자동으로 확인할 수 있으므로 이를 통해 수정 후 코드를 제출할 수 있음

```
pip install mypy
```


## 4. 리스트 컴프리핸션 (List Comprehension)

- 람다 표현식 (lambda expression)

```
list(map(lambda x: x + 10, [1, 2, 3))
```

- "리스트 컴프리헨션"이란 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

```
[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
```

- 리스트 외에도 딕셔너리 등이 가능함

```
a = {}

for key, value in original.items():
	a[key] = value
```

- 이와 같은 코드는 아래와 같이 처리할 수 있음 (딕셔너리 컴프리헨션)

```
a = {key: value for key, value in original.items()}
```


## 5. 제너레이터 (Generator)

- 제너레이터란 루프의 반복(iteration) 동작을 제어할 수 있는 루틴 형태

- e.g.) 임의의 조건으로 숫자 1억 개를 만들어내 계산하는 프로그램을 작성한다고 할때, 제너레이터가 없다면 메모리 어딘가에 만들어낸 숫자 1억 개를 보관하고 있어야함

- 이때 yield 구문을 사용하면 제너레이터를 리턴할 수 있음

- yield 구문은 return을 만나면 값을 리턴하고 함수 동작을 종료하는 기존의 함수와 다르게, 중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때 까지 실행됨

```
def get_natural_number():
	n = 0
	while True:
		n += 1
		yield n
```

- 리턴 값은 제너레이터가 됨

```
print(get_natural_number())
```

- 예를들어 100개의 값을 생성하고 싶다면 아래와 같이 100번동안 next()를 수행하면 됨

```
g = get_natural_number()

for _ in range(0, 100):
	print(next(g))
```

- 아울러 제너레이터는 다음과 같이 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능함

```
def generator():
	yield 1
	yield 'string'
	yield True

g = generator()
print(g)
print(next(g))
print(next(g))
print(next(g))
```


## 6. range

```
print(list(range(5)))
print(range(5))
print(type(range(5)))

for i in range(5):
	print(i, end = ' ')
```

- 만약 생성할 숫자가 100만 개쯤 된다면? 메모리에서 적지 않은 공간을 차지할 것이고 시간도 오래 거릴 것임

- 그러나 제너레이터와 같이 range 클래스만 리턴하면 그렇지 않음

```
a = [n for n in range(1000000)]
b = range(1000000)

print(len(a))
print(len(b))
print(len(a) == len(b))
```

- 하지만 a에는 이미 생성된 값이 담겨 있고, b는 생성해야 한다는 조건만 존재함

```
print(b)
print(type(b))
```

- 이제 둘 사이의 메모리 점유율을 비교해보면 range 클래스를 리턴하는 방식의 장점이 쉽게 와닿을 것임

```
import sys

print(sys.getsizeof(a))
print(sys.getsizeof(b))
```

- 게다가 미리 생성하지 않은 값은 인덱스에 접근이 안될 거라 생각할 수 있으나, 인덱스로 접근 시에는 바로 생성하도록 구현되어 있기 때문에 다음과 같이 리스트와 거의 동일한 느낌으로 사용 가능함

```
print(b[999]) # 999
```


## 7. enumerate

```
a = [1, 2, 3, 2, 45, 2, 5]
print(list(enumerate(a)))
```


## 8. 몫과 나머지

```
print(5 // 3) # 몫
print(5 % 3) # 나머지
```


9. print

- 



