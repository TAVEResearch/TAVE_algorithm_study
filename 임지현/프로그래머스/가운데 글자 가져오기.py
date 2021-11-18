def solution(s):
    i = len(s)//2
    if len(s) % 2 == 0:
      return s[i-1] + s[i]
    else:
      return s[i]
