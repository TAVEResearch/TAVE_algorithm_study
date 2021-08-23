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

-


