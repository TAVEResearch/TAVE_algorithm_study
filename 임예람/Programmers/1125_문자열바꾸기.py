strings=["sun", "bed", "car"]	
n=1	
# return ["car", "bed", "sun"]

strings2=["abce", "abcd", "cdx"]	
n2=2	
# ["abcd", "abce", "cdx"]

def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    return strings

print(solution(strings, n))