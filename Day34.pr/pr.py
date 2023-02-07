# 행복한지 슬픈지 10769
# a = input()

# if a.count(':-)') > a.count(':-('):
#     print('happy')
# elif a.count(':-(') > a.count(':-)'):
#     print('sad')
# elif a.count(':-)') == 0 and a.count(':-(') == 0:
#     print('none')
# else:
#     print('unsure')

# 지능형 기차 2455

# max_p = 0
# lst = []
# for i in range(4):
#     out_p, in_p = map(int, input().split())
#     max_p += in_p
#     max_p -= out_p
#     lst.append(max_p)
# print(max(lst))

# 바이러스 2606
# def dfs(start):
#     global total
#     visited[start] = 1 # 1부터?
#     for i in graph[start]:
#         if visited[i] == 0: # 방문하지 않은 곳이 있다면?
#             dfs(i) # 방문해봐라
#             total += 1
              
# n = int(input()) # 컴퓨터 수
# m = int(input()) # 컴퓨터 쌍의 수
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)


# visited = [0]*(n+1) # 방문 체크
# total = 0 
# dfs(1) # 1부터?
# print(total)

# # 섬의 개수
# direction = [(1, 0), (0, 1), (1, 1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]

# while True:
#     n, m = map(int, input().split())
#     if n == 0 and m == 0:
#         break
#     mat = [list(map(int, input().split())) for _ in range(m)]
    
    