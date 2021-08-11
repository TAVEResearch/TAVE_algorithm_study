```python
def solution(x, n):
    answer = []
    num = 0
    for _ in range(n):
        answer.append(num + x)
        num += x
    return answer
```

