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

- 


