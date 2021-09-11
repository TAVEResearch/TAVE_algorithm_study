# 21장 그리디 알고리즘
## 문제 80 태스크 스케줄러
> 595p

* A에서 Z로 표현된 태스크가 있다. 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 없다. 더 이상 태스크를 실행할 수 없는 경우 아이들(idle) 상태가 된다. 모든 태스크를 실행하기 위한 최소 간격을 출력하라.
* 입력
```
tasks = ["A", "A", "A", "B", "B", "B"], n = 2
```
* 출력
```
8
```
* 설명<br>
A -> B -> idle -> A -> B -> idle -> A -> B

<br><br>

## 문제 80 태스크 스케줄러 풀이
### 풀이1. 우선순위 큐 이용
이 문제 또한 마찬가지로 우선순위 큐를 이용해 그리디하게 풀 수 있는 문제다.<br>
그런데 아이템을 추출한 이후에는 매번 아이템 개수를 업데이트해줘야 한다.<br>
파이썬의 heapq만으로 구현하기에는 상당히 번거로운 작업들이 필요하다. <br>
따라서 여기서는 가능한 한 파이썬답게 간결한 방식으로 풀어보기 위해 Counter 모듈을 사용해 코드를 구현해보자.

<br>

---
* **풀이에 들어가기 전에~**<br>
풀이를 보기 전에 이 풀이를 한눈에 정리해보자.

* **# 1**: for문 돌 때마다 태스크 하나가 실행된다.
* **# 2**: for문을 돌 때마다 빈도수가 높은 태스크의 개수를 센다.
* **# 3**: for문을 돌면서 태스크 하나가 실행되므로 result에 1을 더한다.
* **# 4**: 태스크가 하나 실행되므로 `counter`에서 해당 태스크를 하나 뺀다.
* **# 5**: `counter`가 빌 때까지, 즉 모든 태스크가 실행될 때까지 while문을 반복한다.
* **# 6**: most_common(n + 1) 을 추출하고 n + 1개가 추출될 때는 idle 없이 실행한다. 즉 이 부분에선 `result`에 idle 개수를 더한다.

<br>

```python
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):        # 1
                sub_count += 1                                # 2
                result += 1                                   # 3

                counter.subtract(task)                        # 4
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:                                   # 5
                break

            result += n - sub_count + 1                       # 6

        return result
```

<br>

* **subtract**<br>
subtract()는 각 요소의 값을 각각 빼준다.<br>
```python
>>> a = Counter(a=5, b=3)
>>> b = Counter(b=5, c=2)
>>> a.subtract(b)
>>> a
Counter({'a': 5, 'b': -2, 'c': -2})
```
출처: https://dongdongfather.tistory.com/70

<br><br>

---

<br>

이 문제의 전체 코드는 간단하지만, 사실 여기에는 몇 가지 트릭이 있으며, 직관적으로 알아내기 어려운 부분들이 숨어 있다. 

우선 하나씩 살펴보자. 먼저, 우선순위 큐를 사용해 가장 개수가 많은 아이템부터 하나씩 추출해야 하는데, 문제는 전체를 추출하는 게 아니라 하나만 추출하고 빠진 개수를 업데이트할 수 있는 구조가 필요하다는 점이다.

만약 heapq를 사용한다면 다음과 같은 형태가 될 것이다.
```python
for task, count in collections.Counter(tasks).items():
    heapq.heappush(heap, (-count, task))
    ...
    count, task = heapq.heappop(heap)
    ...
    heapq.heappush(heap, (-count + 1, task))
```
각 태스크의 개수를 Counter로 계산하고 이 값을 힙에 추가한다.<br>
heapq는 최소 힙(Min Heap)만을 지원하기 때문에 최대 힙 효과를 내기 위해 음수로 변환하여 저장한다.<br>
heappop()은 항목 전체가 추출되기 때문에 꺼내서 활용한 이후에는 heappush()로 개수를 줄여(여기서는 음수이기 때문에 +1 을 하여) 다시 추가하는 작업이 필요하다.<br>
이처럼 번거로운 작업들이 필요한데, Counter만으로도 이 같은 일을 간결하게 처리할 수 있다. 파이썬의 Counter 모듈은 매우 막강한 기능들을 지원하기 때문이다.

다음과 같이 간단하게 처리가 가능하다.
```python
counter = collections.Counter(tasks)
for task, _ in counter.most_common():
    counter.subtract(task)
```

* **코드 들여다 보기**<br>
```python
- counter -> Counter({'A': 3, 'B': 3})

- counter.most_common() -> [('A', 3), ('B', 3)]

- task -> key 값 (A,B,..)

- for문 후 counter -> Counter({'A': 2, 'B': 2})
```

<br>

이전의 전체 코드와 같은 역할을 하는 코드인데, 훨씬 더 간결하다.<br>
most_common()은 가장 개수가 많은 아이템부터 출력하는 함수이며, 사실상 최대 힙과 같은 역할을 한다. <br>
그러나 pop()으로 추출되는 것은 아니기 때문에 subtract(task)를 지정해 1개씩 개수를 별도로 줄여나간다. <br>
이처럼 Counter 모듈은 개수를 줄이는 메소드도 지원하기 때문에 매우 편리하다. 

<br><br>

그런데 Counter는 0과 음수도 처리하는 특징이 있다. <br>
원래는 편리한 특징이지만 사실 우리에게는 0 이하는 필요가 없기 때문에, 매번 0 이하인지 체크하거나, 0 이하일 때는 아예 삭제하는 기능이 필요하다. 

다음 코드가 그런 역할을 한다.
```python
counter.subtract(task)
counter += collections.Counter()
```
빈 collection.Counter()를 더하는 것인데, 이렇게 할 경우 0 이하인 아이템을 목록에서 아예 제거해버린다. 매우 유용한 핵(Hack)이다.<br>
물론 실무에서라면 이렇게 코드만 작성해두면 무슨 역할을 하는지 아무도 모를 것이다. <br>
따라서 다음 "# 1"과 같이 간단한 주석을 붙여두는 편이 좋을 것 같다.
```python
# 0 이하인 아이템을 목록에서 완전히 제거  "# 1"
counter += collections.Counter()
```
* **코드 들여다 보기**<br>
```python
tasks = ["A", "A", "A", "B", "B", "B", "C"]
counter = collections.Counter(tasks)  # Counter({'A': 3, 'B': 3, 'C': 1})
for task, _ in counter.most_common():
    counter.subtract(task)            # Counter({'A': 2, 'B': 2, 'C': 0})
    
counter += collections.Counter()      # Counter({'A': 2, 'B': 2})
```
0 이하인 아이템이 완전히 제거됨을 알 수 있다.

<br><br>

또 다른 트릭은 n과 관련된 내용이다. <br>
만약 다음의 입력값을 most_common(n)으로 추출하고, 뒤에 idle을 덧붙이는 형태로 실행한다고 가정해보자.
```python
tasks = ["A", "A", "A", "B", "C", "D"], n = 2
```
이 입력값의 경우 실행 결과는 다음과 같을 것이다.
```
A -> B -> idle -> A -> C -> idle -> A -> D
```
```
A _ _ A _ _ A 
```
결과는 8 이다. 정답일까? 그렇지 않다.

아래와 같은 순서대로 실행할 경우 7 로, 한 번 더 줄일 수 있기 때문이다.
```
A -> B -> idle -> A -> C -> D -> A
```
이 경우 마지막에는 순서가 다르게 나와야 하는데, 앞 부분과 달리 마지막에만 순서가 다르게 나오게 하는 일은 별도의 예외 처리가 필요하다.<br>

**-> n 이 아닌 n + 1만큼을 추출한다.**<br>
즉 most_common(n + 1) 을 추출하고 n + 1개가 추출될 때는 idle 없이 실행한다. 

결과는 다음과 같다.
```
A -> B -> C -> A -> D -> idle -> A
```
입력값이 n = 2 였기 때문에 n + 1을 추출했을 때 3개가 모두 나온다면 idle 없이 계속 진행한다. <br>
그다음에는 A -> D 2개만 추출됐기 때문에 한 번 idle하고 마지막으로 A를 출력한다.<br>
앞서와 순서는 달라졌지만 정답은 7로 동일하다. <br>
이렇게 하면 별도의 예외 처리 없이도 쉽게 계산이 가능하다. n + 1 부분이 핵심이다.

<br><br><br>
