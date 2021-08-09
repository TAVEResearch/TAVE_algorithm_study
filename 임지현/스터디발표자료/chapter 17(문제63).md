## 문제 63 색 정렬
> 508p

* 빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리(In-Place) 정렬을 수행하라.
* 입력
```
[2,0,2,1,1,0]
```
* 출력
```
[0,0,1,1,2,2]
```

<br>

---
이 문제의 포인트는 다음과 같다.
1. 0은 리스트의 왼쪽으로, 2는 리스트의 오른쪽으로 이동한다.
2. 값이 0일 땐 왼쪽으로, 1일 땐 continue, 2일 땐 오른쪽으로 이동하면서 스왑한다.

### 문제 63 내가 짠 코드
```python
def solution(nums):
  red, white = 0, 0
  blue = len(nums) - 1

  while white <= blue:
    if nums[white] == 0:
      nums[white], nums[red] = nums[red], nums[white]
      white += 1
      red += 1
    elif nums[white] == 2:
      nums[white], nums[blue] = nums[blue], nums[white]
      white += 1
      blue -= 1  # 1
    else:
      white += 1
  
  return nums

nums = [2,0,2,1,1,0]
print(solution(nums))
```

* **# 1**: blue가 왼쪽으로 이동하는 이유는 방금 nums[blue]는 2가 되었고, 왼쪽으로 이동을 해야 다음 번에 nums[white]가 2일 때, 스왑을 하여 2가 오른쪽에 몰릴 수 있기 때문이다.

<br><br>

### 제자리 정렬이란?
* 제자리 정렬을 사용하면 정렬할 대상이 담겨 있는 변수 자체를 정렬된 형태로 바꿔 버린다. 기존의 정렬되기 전의 모습은 잃게 되는 것이다.<br>
* 즉, 정렬된 결과를 assign할 l-value는 필요없다.
```python
a = [2, 1, 5, 4, 3]
a.sort()
print(a)  # [1, 2, 3, 4, 5]
```

https://blog.naver.com/jhiya7420/222357270970

<br><br>
