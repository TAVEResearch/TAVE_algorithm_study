# 목차
* [chapter 6. 문자열 조작](#6장-문자열-조작)
* [References](#references)

<br><br>

<img src="https://user-images.githubusercontent.com/55045377/116873723-1a64aa80-ac53-11eb-8d03-5df57948b42d.jpg">

<br>

---

<br>

# 6장 문자열 조작
> 문자열 조작(String Manipulation)이란 문자열을 변경하거나 분리하는 등의 여러 과정을 말한다.

<br>

파이썬에서 문자열을 조작하는 메서드는 여러 가지가 있다.<br>
* **문자열 바꾸기**
  * **[replace](#replace)**
  * **[translate](#translate)**
* **문자열 분리하기**
  * **[split](#split)**
* **구분자 문자열과 문자열 리스트 연결하기**
  * **[join](#join)**
* **소문자를 대문자로 바꾸기**
  * **[upper](#upper)**
* **대문자를 소문자로 바꾸기**
  * **[lower](#lower)**
* **왼쪽 공백 삭제하기/왼쪽의 특정 문자 삭제하기**
  * **[lstrip](#lstrip)**
* **오른쪽 공백 삭제하기/오른쪽의 특정 문자 삭제하기**
  * **[rstrip](#rstrip)**
* **양쪽 공백 삭제하기/양쪽의 특정 문자 삭제하기**
  * **[strip](#strip)**
* **문자열을 왼쪽 정렬하기**
  * **[ljust](#ljust)**
* **문자열을 오른쪽 정렬하기**
  * **[rjust](#rjust)**
* **문자열을 가운데 정렬하기**
  * **[center](#center)**
* **문자열 왼쪽에 0 채우기**
  * **[zfill](#zfill)**
* **문자열 위치 찾기**
  * **[find](#find)**
* **오른쪽에서부터 문자열 위치 찾기**
  * **[rfind](#rfind)**
* **문자열 위치 찾기**
  * **[index](#index)**
* **오른쪽에서부터 문자열 위치 찾기**
  * **[rindex](#rindex)**
* **문자열 개수 세기**
  * **[count](#count)**
  
<br><br>


## replace
**replace('바꿀문자열', '새문자열')** 은 문자열 안의 문자열을 다른 문자열로 바꾼다.<br>
```python
s = 'Hello, world!'
print(s.replace('world!', 'Python'))
```
```
Hello, Python
```
문자열 자체는 변경하지 않으며 바뀐 결과를 반환한다.
```python
s = 'Hello, world!'
s.replace('world!', 'Python')
print(s)
```
```
Hello, world!
```

<br>

## translate
**translate**는 문자열 안의 문자를 다른 문자로 바꾼다.<br>
먼저 str.maketrans('바꿀문자', '새문자')로 변환 테이블을 만든다. 그다음에 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환한다. 
```python
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)
```
```
'1ppl2'
```

<br>

## split
**split()** 은 공백을 기준으로 문자열을 분리하여 리스트로 만든다.<br>
```python
'apple pear grape pineapple orange'.split()
```
```
['apple', 'pear', 'grape', 'pineapple', 'orange']
```
**split('기준문자열')** 과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리한다.
```python
'apple, pear, grape, pineapple, orange'.split(', ')
```
```
['apple', 'pear', 'grape', 'pineapple', 'orange']
```

<br>

## join
**join(리스트)** 는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만든다.<br>
```python
# 공백
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
```
```
'apple pear grape pineapple orange'
```
```python
# 마이너스 '-'
'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
```
```
'apple-pear-grape-pineapple-orange'
```

<br>

## upper
**upper()** 는 문자열의 문자를 모두 대문자로 바꾼다.<br>
```python
'python'.upper()
```
```
'PYTHON'
```

<br>

## lower
**lower()** 는 문자열의 문자를 모두 소문자로 바꾼다.<br>
```python
'PYTHON'.lower()
```
```
'python'
```

<br>

## lstrip
**lstrip()** 은 문자열에서 왼쪽에 있는 연속된 모든 공백을 삭제한다.<br>
```python
'   Python   '.lstrip()
```
```
'Python   '
```
**lstrip('삭제할문자들')** 과 같이 삭제할 문자들을 문자열 형태로 넣어주면 문자열 왼쪽에 있는 해당 문자를 삭제한다. 단, 여기서는 공백을 넣지 않았으므로 공백은 그대로 둔다.<br>
```python
', python.'.lstrip(',.')
```
```
' python.'
```

<br>

## rstrip
**rstrip()** 은 문자열에서 오른쪽에 있는 연속된 모든 공백을 삭제한다.<br>
```python
'   Python   '.rstrip()
```
```
'   Python'
```
**rstrip('삭제할문자들')** 과 같이 삭제할 문자들을 문자열 형태로 넣어주면 문자열 오른쪽에 있는 해당 문자를 삭제한다. 마찬가지로 공백을 넣지 않았으므로 공백은 그대로 둔다.<br>
```python
', python.'.rstrip(',.')
```
```
', python'
```

<br>

## strip
**strip()** 은 문자열에서 양쪽에 있는 연속된 모든 공백을 삭제한다.<br>
```python
'   Python   '.strip()
```
```
'Python'
```
**strip('삭제할문자들')** 과 같이 삭제할 문자들을 문자열 형태로 넣어주면 문자열 양쪽에 있는 해당 문자를 삭제한다. 여기서도 공백을 넣지 않았으므로 공백은 그대로 둔다.<br>
```python
', python.'.strip(',.')
```
```
' python'
```

<br>

## ljust
**ljust(길이)** 는 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 남는 공간을 공백으로 채운다.<br>
```python
'python'.ljust(10)
```
```
'python    '
```

<img src="https://dojang.io/pluginfile.php/13715/mod_page/content/3/024001.png" width=60%>


## rjust
**rjust(길이)** 는 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하며 남는 공간을 공백으로 채운다.<br>
```python
'python'.rjust(10)
```
```
'    python'
```

<img src="https://dojang.io/pluginfile.php/13715/mod_page/content/3/024002.png" width=60%>


## center
center(길이)는 문자열을 지정된 길이로 만든 뒤 가운데로 정렬하며 남는 공간을 공백으로 채운다.<br>
```python
'python'.center(10)
```
```
'  python  '
```

<img src="https://dojang.io/pluginfile.php/13715/mod_page/content/3/024003.png" width=60%>

## zfill
**zfill(길이)** 는 지정된 길이에 맞춰서 문자열의 왼쪽에 0을 채운다.<br>
```python
>>> '35'.zfill(4)        # 숫자 앞에 0을 채움
'0035'
>>> '3.5'.zfill(6)       # 숫자 앞에 0을 채움
'0003.5'
>>> 'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음
'00000hello'
```

<br>

## find
**find('찾을문자열')** 은 문자열에서 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환한다. find는 왼쪽에서부터 문자열을 찾는데, 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다.
```python
>>> 'apple pineapple'.find('pl')
2
>>> 'apple pineapple'.find('xy')
-1
```

<br>

## rfind
**rfind('찾을문자열')** 은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환한다. 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다.
```python
>>> 'apple pineapple'.rfind('pl')
12
>>> 'apple pineapple'.rfind('xy')
-1
```

<br>

## index
**index('찾을문자열')** 은 왼쪽에서부터 특정 문자열을 찾아서 인덱스를 반환한다. 단, 문자열이 없으면 에러를 발생시킨다. index도 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다.
```python
>>> 'apple pineapple'.index('pl')
2
```

<br>

## rindex
**rindex('찾을문자열')** 은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환한다. 마찬가지로 문자열이 없으면 에러를 발생시키며, 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다.
```python
>>> 'apple pineapple'.rindex('pl')
12
```

<br>

## count
count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아낸다.
```python
>>> 'apple pineapple'.count('pl')
2
```

<br><br>











---

# References
* https://dojang.io/mod/page/view.php?id=2299

<br><br>
