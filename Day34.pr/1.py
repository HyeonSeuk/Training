def dfs(start):
    global total
    visited[start] = 1 # 1부터?
    for i in graph[start]:
        if visited[i] == 0: # 방문하지 않은 곳이 있다면?
            dfs(i) # 방문해봐라
            total += 1
              
n = int(input()) # 컴퓨터 수
m = int(input()) # 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [0]*(n+1) # 방문 체크
total = 0 
dfs(1) # 1부터?
print(total)