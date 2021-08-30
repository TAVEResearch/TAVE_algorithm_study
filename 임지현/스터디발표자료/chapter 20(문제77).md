## 문제 77 가장 긴 반복 문자 대체
> 581p

* 대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.
* 입력
```
s = "AAABBC", k = 2
```
* 출력
```
5
```
* 설명<br>
  B를 A로 각각 2번 변경하면 길이 5인 AAAAA를 만들 수 있다.
  
<br><br>

### 문제 77 내가 구현한 코드
풀이를 보고 코드를 구현했다.<br>
```python
import collections

def solution(s,k):
  left, right = 0, 0
  counts = collections.Counter()

  for right in range(1, len(s) + 1):
    counts[s[right-1]] += 1
    most_char_cnt = counts.most_common(1)[0][1]
    
    if right - left - most_char_cnt > k:
      counts[s[left]] -= 1
      left += 1
  return right - left

s = "AAABBC"
k = 2
print(solution(s,k))
```

<br><br>

## 문제 77 가장 긴 반복 문자 대체 풀이
### 풀이1. 투 포인터, 슬라이딩 윈도우, Counter를 모두 이용
이 문제는 오른쪽 포인터가 계속 우측으로 이동한다는 점에서 슬라이딩 윈도우 문제이지만, 왼쪽 포인터를 계속 좁혀서 범위를 조절해 나간다는 점에서는 76번 문제와 마찬가지로 투 포인터와 결합된 문제로 볼 수 있다.

[-> 슬라이딩 윈도우와 투 포인터의 차이점](https://github.com/jadeneu/TIL/blob/main/Python%20Algorithm/chapter%2020_01(%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9%20%EC%9C%88%EB%8F%84%EC%9A%B0%2C%20%EB%AC%B8%EC%A0%9C75).md#20%EC%9E%A5-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9-%EC%9C%88%EB%8F%84%EC%9A%B0)

<br>

---

* **풀이에 들어가기 전에~**<br>
풀이를 보기 전에 이 풀이를 한눈에 정리해보자.
1. 슬라이딩 윈도우는 항상 오른쪽으로 한 칸씩 이동한다.
2. 현재 슬라이딩 윈도우에 들어있는 값들의 수를 계산한다.
3. 슬라이딩 윈도우의 크기 - 가장 큰 비중의 값의 갯수 = 바꿔야하는 갯수이다.
4. 만약, 바꿔야하는 갯수가 k보다 크다면 현재 슬라이딩 윈도우는 불가하므로 왼쪽을 증가시켜 슬라이딩 윈도우의 크기를 줄인다.
5. k가 크거나 같다면 현재 윈도우와 최대 윈도우의 크기를 비교해 최대 윈도우를 갱신시킨다. (생략 가능)

<br>

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
```

<br><br>

* **생략된 최대 윈도우의 크기 갱신 코드**
```python
max_len = max(right - left, max_len)
```

<br>

---

<br>

이제 풀이를 자세히 살펴보자.

```python
left = right = 0
counts = collections.Counter()
for right in range(1, len(s) + 1):
    counts[s[right - 1]] += 1
    max_char_n = counts.most_common(1)[0][1]
    ...
```
왼쪽 포인터와 오른쪽 포인터를 0으로 지정한 다음에 오른쪽 포인터 right는 계속 우측으로 한 칸씩 이동한다. <br>
이때 Counter()를 이용해 가장 흔하게 등장하는 문자의 값을 계산해 나간다.

<br>

* **counts.most_common(1)[0][1] 살펴보기**
```python
counts = collections.Counter("AAABB")
```
```python
>>> counts
Counter({'A': 3, 'B': 2})
>>> counts.most_common()
[('A', 3), ('B', 2)]
>>> counts.most_common(1)
[('A', 3)]
>>> counts.most_common(1)[0]
('A', 3)
>>> counts.most_common(1)[0][1]
3
```
이 같은 과정을 통해, 가장 흔하게 등장하는 문자의 개수를 가져오게 된다.

<br>

```python
if right - left - max_char_n > k:
    counts[s[left]] -= 1
    left += 1
```
오른쪽 포인터는 계속 커지기 때문에 최랫값을 추출하기 위해서는 왼쪽 포인터는 0에서 움직이지 않는 게 가장 좋다.<br>
그러나 k 연산 횟수를 넘어선다면 left += 1과 같이 왼쪽 포인터를 1 더 크게 한다. 

이제 마지막으로 최대 길이가 되는 값을 찾는다.
```python
max_len = max(right - left, max_len)
```
오른쪽 포인터에서 왼쪽 포인터를 뺀 값이 가장 긴 길이가 되는 값이다.<br>
즉 오른쪽 포인터는 가능한 한 크게 하고 왼쪽 포인터는 가능한 한 작게 하는 값이 된다. <br>
그런데 이 부분은 생략이 가능하다. 한번 최댓값이 된 상태에서는 오른쪽 포인터가 한 칸 이동하면 왼쪽 포인터도 따라서 이동하게 되면서 max_len 값은 바뀌지 않기 때문이다.<br>
따라서 최댓값을 구하는 부분은 생략할 수 있다.

이제 전체 코드는 다음과 같이 정리할 수 있다.
```python
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
```
<br><br>





















---
# References
* https://velog.io/@pyh8618/LeetCode-424.-Longest-Repeating-Character-Replacement

<br><br><br>
