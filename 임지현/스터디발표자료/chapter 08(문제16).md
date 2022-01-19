## 문제 16 두 수의 덧셈
> 221p

* 역순으로 저장된 연결 리스트의 숫자를 더하라.
* 입력
```
(2 -> 4 -> 3) + (5 -> 6 -> 4)
```
* 출력
```
7 -> 0 -> 8
```
* 설명<br>
342 + 465 = 807

<br><br>

## 문제 16 두 수의 덧셈 풀이
### 풀이1. 자료형 변환
연결 리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고, 이를 모두 계산한 후 다시 연결 리스트로 바꾸는 방법을 써보자.

먼저, 역순으로 된 연결 리스트를 뒤집어야 한다.<br>
(반복 풀이 방식) ↓
```python
def reverseList(self, head: ListNode) -> ListNode:
  node, prev = head, None
  
  while node:
    next, node.next = node.next, prev
    prev, node = node, next
    
  return prev
```

<br>

이번에는 덧셈 연산을 위해 연결 리스트를 파이썬의 리스트로 변경해야 한다.
```python
def toList(self, node: ListNode) -> List:
  list: List = []
  while node:
    list.append(node.val)
    node = node.next
  return list
```
이 코드는 node를 반복하며 값을 리스트에 추가하는 함수다.

반대로 리스트를 연결 리스트로 변경하는 함수도 작성해보자.
```python
def toReversedLinkedList(self, result: str) -> ListNode:
  prev: ListNode = None
  for r in result:
    node = ListNode(r)
    node.next = prev
    prev = node
    
  return node
```
이 코드는 순서대로 엮어 나가는 방식으로 구현했는데, 이렇게 하면 뒤집힌 연결 리스트가 된다.<br>
이 문제에서는 출력 또한 역순으로 하도록 문제에서 요구하고 있으므로 이 상태로 그대로 내보내면 된다.

이제 실제로 덧셈 풀이를 작성해보자.
```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  a = self.toList(self.reverseList(l1))
  b = self.toList(self.reverseList(l2))
```
이 코드에서는 먼저 연결 리스트를 뒤집었고, 이를 다시 파이썬 리스트로 변환했다.<br>
따라서 a와 b는 각각 뒤집힌 연결 리스트의 파이썬 리스트가 될 것이다.

이제 덧셈 연산을 하면 되는데 이를 위해서는 리스트를 int 형태로 결합해야 한다.
```python
resultStr = int(''.join(str(e) for e in a)) +
            int(''.join(str(e) for e in b))
```
현재 이 리스트는 문자열이 아닌 숫자형 리스트며, 따라서 이를 합치기 위해서는 문자형으로 먼저 변경이 필요하다.<br>
여기서는 str(e)로 각 항목을 문자로 변경한 다음 join()으로 합쳤다. 그런데 덧셈 연산을 위해서는 다시 숫자형이 되어야 한다.<br>
따라서 최종 값은 int로 다시 변경해줘야 한다.

마지막으로, 최종 계산 결과를 연결 리스트로 바꿔보자.<br>
앞서 만들어둔 toReversedLinkedList()를 사용하면 쉽게 변환할 수 있을 것 같다.<br>
단 여기서는 문자열을 입력값으로 받기 때문에 다음과 같이 str()로 한 번 변환하는 작업은 필요하다.
```python
return self.toReversedLinkedList(str(resultStr))
```
<br>

이제 모두 통합하면 전체 코드는 다음과 같다.
```python
class Solution:
  # 연결 리스트 뒤집기
  def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
      next, node.next = node.next, prev
      prev, node = node, next

    return prev
    
  # 연결 리스트를 파이썬 리스트로 변환
  def toList(self, node: ListNode) -> List:
    list: List = []
    while node:
      list.append(node.val)
      node = node.next
    return list
    
  # 파이썬 리스트를 연결 리스트로 변환
  def toReversedLinkedList(self, result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
      node = ListNode(r)
      node.next = prev
      prev = node

    return node
    
  # 두 연결 리스트의 덧셈
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))
    
    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))
                
    # 최종 계산 결과 연결 리스트 변환
    return self.toReversedLinkedList(str(resultStr))
```
<br><br>

### 풀이2. 전가산기 구현
여기서는 논리 회로의 전가산기(Full Adder)와 유사한 형태를 구현해보자.<br>
이진법이 아니라 십진법이라는 차이만 있을 뿐, 자리올림수(Carry)를 구하는 것까지 가산기의 원리와 거의 동일하다.<br>
전가산기의 진리표와 회로도는 다음 그림 8-5와 같다.

<img src="https://user-images.githubusercontent.com/55045377/150140610-d341a0bb-6d2a-49e7-8e30-49acfa3210a0.png" width=60%>

입력값 A와 B, 이전의 자리올림수(Carry in) 이렇게 3가지 입력으로 합(Sum)과 다음 자리올림수(Carry out) 여부를 결정한다.<br>
그림 8-5에서 우측 그림은 전가산기 회로도를 나타낸다.<br>
입력값 A, B는 오른쪽으로는 XOR 게이트를 통과한 결과가 나아가고, 아래로는 AND 게이트를 통과한 결과가 나아간다. 그렇게 합과 다음 자리올림수 위치에 도달한 결과가 그림 좌측의 진리표다.<br>
실제로 덧셈 연산을 수행하는 논리 회로의 원리며, 산술 논리 장치를 구성하는 디지털 회로의 일부분이다. 산술 논리 장치는 컴퓨터의 중앙 처리 장치, 그러니까 우리가 잘 아는 CPU의 한 부분이기도 하다.<br>
* **참고**<br>
  + Sum은 A와 B의 XOR을 한 뒤에 다시 Carry in과 XOR을 한 값이다. 왜냐하면 XOR은 두 개가 다를시 1을 반환하기 때문에 결국 더했을 때 그 자리에 올 수와 같다. 즉 A, B를 XOR하고 그 값을 Carry in과 XOR을 하면 sum(그자리에 올 0 or 1)값이 된다.

  + Carry out은 A와 B가 둘다 1이어서 밑의 AND 연산으로 1이되고, 그 밑의 or 연산으로 1이되어 올림수가 발생하는 경우와 또 다른 하나는 A와 B의 XOR 연산 즉 둘 중 하나만 1이어서 XOR로 1이 되고, Carry in이 1이되어서 그 밑의 AND연산으로 1, 그 밑의 or 연산으로 최종 1이 반환되어 올림수가 발생하는 경우 이렇게 2가지이다.
<br>

여기서는 연산 결과로 나머지를 취하고 몫은 자리올림수 형태로 올리는 전가산기의 전체적인 구조만 참고해 풀이해본다.
<br>

```python
sum = 0
if l1:
  sum += l1.val
  l1 = l1.next
if l2:
  sum += l2.val
  l2 = l2.next
```
이 코드에서 먼저, 두 입력값의 합을 구한다. l1, l2는 그럼 8-5의 오른쪽 전가산기 회로도에서 A, B의 역할과 동일하다.<br>
두 입력값의 연산을 수행하고 다음과 같이 자릿수가 넘어갈 경우에는 자리올림수를 설정할 것이다.
```python
carry, val = divmod(sum + carry, 10)
```
이처럼 자리올림수를 계산하게 되는데, 전가산기와 마찬가지로 이전의 자리올림수 carry를 받아오고, 이를 divmod()로 계산한다.<br>
divmod()는 파이썬의 내장 함수로, 몫과 나머지로 구성된 튜플을 리턴한다. 즉 다음과 같이 (a // b, a % b)와 동일한 결과를 출력한다.
```python
>>> divmod(10, 3)
(3, 1)
>>> (10 // 3, 10 % 3)
(3, 1)
```
<br>

다시 문제로 돌아와 carry, val = divmod(sum + carry, 10)을 하게 되면, 가산 결과가 두 자릿수가 될 경우 몫은 자리올림수로 설정해 다음번 연산에 사용되게 하고 나머지는 값으로 취한다.<br>
이제 이 값을 연결 리스트로 만들어 주면 된다.<br>
원래 가산기는 논리 회로를 이용해 이진 연산을 수행하지만 여기서는 전체적인 구조만 참고하여 십진 연산에 응용해봤다.<br>
전체 코드는 다음과 같다.
```python
# 입력: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 출력: 7 -> 0 -> 8

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  root = head = ListNode(0)
  
  carry = 0
  while l1 or l2 or carry:
    sum = 0
    # 두 입력값의 합 계산
    if l1:
      sum += l1.val
      l1 = l1.next
    if l2:
      sum += l2.val
      l2 = l2.next
      
    # 몫(자리올림수)과 나머지(값) 계산
    carry, val = divmod(sum + carry, 10)
    head.next = ListNode(val)
    head = head.next
    
  return root.next
```
* 실제 돌려볼 수 있는 코드
```python
class Node(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class LinkedList():
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
      root = head = Node(0)
      
      carry = 0
      while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
          sum += l1.val
          l1 = l1.next
        if l2:
          sum += l2.val
          l2 = l2.next
          
        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = Node(val)
        head = head.next
        
      return root.next



q = LinkedList()
n1 = Node(3)
n2 = Node(4, n1)
n3 = Node(2, n2)

m1 = Node(4)
m2 = Node(6, m1)
m3 = Node(5, m2)

print(q.addTwoNumbers(n3,m3))
```
<br><br>

