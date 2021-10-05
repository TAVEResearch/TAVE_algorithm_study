# 목차
* [chapter 23. 다이나믹 프로그래밍](#23장-다이나믹-프로그래밍)
  + [문제 86 최대 서브 배열](#문제-86-최대-서브-배열)
    - [문제 86 내가 구현한 코드](#문제-86-내가-구현한-코드)
  + [문제 86 최대 서브 배열 풀이](#문제-86-최대-서브-배열-풀이)
    - [풀이1. 메모이제이션](#풀이1-메모이제이션)
      - [메모이제이션이란?](#-메모이제이션이란)
    - [풀이2. 카데인 알고리즘](#풀이2-카데인-알고리즘)
---
* [References](#references)

<br><br><br>

# 23장 다이나믹 프로그래밍
## 문제 86 최대 서브 배열
> 636p

* 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
* 입력
```
[-2,1,-3,4,-1,2,1,-5,4]
```
* 출력
```
6
```
* 설명<br>
[4,-1,2,1]은 합 6으로 가장 큰 서브 배열이다.

<br><br>

### 문제 86 내가 구현한 코드
```python
def solution(arr):
  max_arr = []
  max_arr.append(arr[0])           # 1
  for i in range(len(arr)-1):      # 2
    sum = max_arr[i] + arr[i+1]
    if arr[i+1] < sum:
      max_arr.append(sum)
    else:
      max_arr.append(arr[i+1])

  return max(max_arr)              # 3

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(solution(arr))
```
`arr`의 요소를 차례대로 둘씩 더하면서 더한 값이 원래 요소 값보다 크면 계속 다음 요소 값을 더하면서 값을 늘리고,<br>
더한 값보다 원래 요소 값이 더 크면 그대로 둬서 더 큰 값이 갱신되도록 하는 코드이다.

<br>

코드를 자세히 설명하면 아래와 같다.

* **# 1**: `arr`의 첫번째 요소를 `max_arr`에 넣는다. 나중에 for문을 돌면서 `arr`의 요소의 합과 크기 비교를 하기 위한 처리다.
* **# 2**: for문에서 `i+1`번째 인덱스까지 보기 때문에 range를 `len(arr)-1`로 둔다.
* **# 3**: 값 갱신이 끝나면(for문이 끝나면) 갱신 값들 중 가장 큰 값을 return 한다.

<br><br>

## 문제 86 최대 서브 배열 풀이
### 풀이1. 메모이제이션

<br>

#### ✅ 메모이제이션이란?
메모이제이션(memoization)은 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.

<br><br>

피보나치 수열을 예로 들어보자.<br>

---
* **피보나치 수열**<br>
피보나치 수는 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다. (편의상 0번째 항을 0으로 두기도 함)

<img src="https://user-images.githubusercontent.com/55045377/135254677-90d5d23f-c7ed-4efe-9314-743e5be35709.png" width=40% height=40%>

---

<br><br>

피보나치 수열을 구하는 가장 단순한 방법은 다음과 같다.<br>
* 피보나치 수열의 n번째 항을 구하는 함수
```c
fib(n) {
   if n is 1 or 2, return 1;
   return fib(n-1) + fib(n-2);
}
```
fib 함수가 재귀적으로 실행되면서 같은 인자값에 대해 여러번 실행하게 된다. 

<img src="https://user-images.githubusercontent.com/55045377/135256442-01944e84-02a5-4fdd-8d95-2eb943d80f20.png">

<br>

이때 메모이제이션을 통해 반복 작업을 피할 수 있다.
```
1. memo 배열을 만들어 0으로 초기화한다. (파이썬의 경우 빈 리스트 or 딕셔너리 memo 생성)
2. memo[1]과 memo[2]를 각각 1로 초기화한다.
```
```c
fib(n) {
   if memo[n] is zero:
       memo[n] = fib(n-1) + fib(n-2);
   return memo[n];
}
```

<img src="https://user-images.githubusercontent.com/55045377/135257737-b0150535-7426-4c07-b4dd-921acef3cc7c.png">

<br>

---

<br>

이제 풀이를 살펴보자.

<br>

메모이제이션을 이용해 그림 23-8과 같은 결과를 만들 수 있다.

<img src="https://user-images.githubusercontent.com/55045377/135258531-80692744-3500-4524-aaa4-18aa6c553f1f.png" width=50% height=50%>

앞에서부터 계속 값을 계산하면서 누적 합을 계산한다. 이전 값을 계속 더해나가되 0 이하가 되면 버린다.<br>
* **최댓값을 찾아야 하므로 0 이하인 값은 서브 배열에 포함시키지 않는다!**

```python
def maxSubArray(self, nums: List[int]) -> int:
    sums: List[int] = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        
    return max(sums)
```
이렇게 메모이제이션으로 값을 더해 나간 sums에서 최댓값을 추출하면 서브 배열의 최댓값을 찾을 수 있다.<br>
여기서 sums라는 별도 변수를 사용했는데 가만히 살펴보면 추가 변수가 없이도 충분히 처리가 가능할 것 같다.

전체 코드는 다음과 같다.
```python
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
```
기존 nums에 합을 함께 넣었다. 공간을 재활용하여 공간 복잡도를 없앴고, 풀이도 좀 더 깔끔해졌다.

<br><br>

### 풀이2. 카데인 알고리즘
제이 카데인(Jay Kadane)이 O(n)에 풀이가 가능하도록 고안한 카데인 알고리즘(Kadane's Algorithm)이라는 좋은 해법이 있다.

당시 그는 최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2) 풀이에서 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제 O(n) 풀이로 치환해서 풀이했다.

전체 풀이 코드는 다음과 같다.
```python
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum
```
이전 풀이에서는 매번 계산해서 넣기만 하고 마지막에 max()를 전체 계산해서 가져오게 했지만 당시 제이 카데인은 이런 형태로 매번 best_sum을 계산하게 했다.<br>
하지만 사실상 동일한 코드로 볼 수 있으며, 속도 또한 양쪽 모두 동일하다.





























<br><br>


---
# References
* https://ssminji.github.io/2020/02/05/the-cake-thief/
* https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98

<br><br><br>

