#https://dndi117.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%83%90%EC%83%89BFSDFS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98-%EA%B8%B0%EC%B4%88#recentComments
n, m = 7, 8

#만약 n개만큼의 정점이 존재하고, m개만큼의 입력을 받는다면 
graph = [[] for _ in range(n+1)] # n+1개만큼의 공간을 만들어서 graph[n]이 n번 정점을 나타내도록 해 준다 

for _ in range(m):
    x,y = map(int, input().split()) 
    graph[x].append(y) 
    graph[y].append(x) 

print(graph)

graph0 = {
    1 : [2,3,4], 
    2 : [5], 
    3 : [5], 
    4 : [], 
    5 : [6, 7], 
    6 : [], 
    7 : [3]
}

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    print(discoverd)
    for w in graph[v]:
        if not w in discoverd:
            discoverd = recursive_dfs(w, discovered)
    return discovered

# [1]
# [1, 2]
# [1, 2, 5]
# [1, 2, 5, 6]
# [1, 2, 5, 6, 7]
# [1, 2, 5, 6, 7, 3]
# [1, 2, 5, 6, 7, 3, 4]
# [1, 2, 5, 6, 7, 3, 4]

def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        print(discovered, queue)
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

# [1] [1]
# [1, 2, 3, 4] [2, 3, 4]
# [1, 2, 3, 4, 5] [3, 4, 5]
# [1, 2, 3, 4, 5] [4, 5]
# [1, 2, 3, 4, 5] [5]
# [1, 2, 3, 4, 5, 6, 7] [6, 7]
# [1, 2, 3, 4, 5, 6, 7] [7]
# [1, 2, 3, 4, 5, 6, 7]
