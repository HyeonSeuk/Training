# 별찍기 - 4
# a = int(input())
# for i in range(a, 0, -1):
#     print(('*'*i).rjust(a))

# 대표값
# from collections import Counter
# lst = []
# for i in range(10):
#     a = int(input())
#     lst.append(a)
# counter = Counter(lst)
# most = counter.most_common(2)

# print(sum((lst))//10)
# print(most[0][0])

# 새로 읽기
# mat = []

# for _ in range(5):
#     line = list(input())
#     mat.append(line)
  
# for i in range(max(len(a) for a in mat)):
#     for j in range(5):
#         if i < len(mat[j]):
#             pass
#             print(mat[j][i], end='')

# 박스

        
# 누울 자리를 찾아라
# a = int(input())
# room = [list(input()) for _ in range(a)]
# x, y = 0, 0
# for i in range(a):
#     cnt = 0
#     for j in range(a):
#         if room[i][j] == '.':
#             cnt += 1
#             if cnt == 2:
#                 x += 1
#         else:
#             cnt = 0
# for i in range(a):
#     cnt = 0
#     for j in range(a):
#         if room[j][i] == '.':
#             cnt += 1
#             if cnt == 2:
#                 y += 1
#         else:
#             cnt = 0
# print(x, y)