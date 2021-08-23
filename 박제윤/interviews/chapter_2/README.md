## 1. 통계로 본 코테 선호도 (p55) 

- 코테에 가장 효율적인 언어는 C++이지만, 코딩해야되는 라인 수가 길음
- 파이썬은 그에 비해 훨씬 짧은 라인만으로도 기능 구현이 가능함
- 코테 합격률은 두 언어가 근소한 차이정도만 가짐


## 2. Generic Programming (p58)

- Generic이란 파라미터 타입이 나중에 지정 (to be specified later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일
- 파이썬은 원래 동적 타이핑(Dynamic Typing) 언어이기 때문에 제네릭이 필요없음
- 하지만 동적 타이핑의 장점이자 단점은 얼핏 사용하기엔 매우 편하지만, 코드의 복잡도가 높아질 수록 혼란을 가중시킨다는 점임
- 따라서 타입을 명시해주면 가독성을 높이고 버그 발생 확률을 낮출 수 있음

```
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool:
	return a == b

are_equal(10, 10.0)
```

## 3. 추상 자료형 (ADT, Abstract Data Type)

```
from collections import namedtuple

MyStruct = namedtuple("MyStruct", "field1 field2 field3")

m = MyStruct("foo", "bar", "baz")
```

- 파이썬에는 구조체가 없을 뿐더러 클래스 또한 데이터 타입을 지정할 수 없어서 구조체와 같은 형태를 정의하려면 네임드 튜플을 사용해야했음

- 파이썬 3.7부터는 "dataclass"를 지원하며, @dataclass 데코레이션(decoration)으로 타입 힌트와 함께 활용함으로써 다음과 같이 class를 이용해 구조체 형태롤 정의할 수 있음

```
# pip install dataclasses
from dataclasses import dataclass

@dataclass
class Product:
	weight: int = None
	price: float = None

apple = Product()
apple.price = 10  
```

## 4. Class

```
from dataclasses import dataclass

@dataclass
class Rectangle:
	width: int
	height: int

	def area(self):
		return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())
```

- dataclass를 선언하게 되면 여러가지 내부 함수의 기능도 자동으로 구현해주기 때문에 편리하게 활용할 수 있음


## 5. 결론

- C++가 서비스의 주력 언어로 쓰이는 일이 드물고 주로 코어 모듈 쪽에 사용되다 보니 코어 개발을 해본 면접관이 아니라면 실제로는 문법을 제대로 알지 못할 가능성이 큼

- C++와 JAVA를 수도코드로 쓰기엔 지나치게 산만함(verbose)

- "파이썬 짱"

