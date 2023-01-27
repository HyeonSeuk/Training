# 세 수
# a = list(map(int, input().split()))
# a.sort()
# print(a[1])

# 고무오리 디버깅
# s = input()
# n = 0
# while True:
#     q = input()
#     if q == '고무오리 디버깅 끝':
#         break
#     else:
#         if q == '문제':
#             n += 1
#         elif q == '고무오리':
#             if n == 0:
#                 n += 2
#             else:
#                 n -= 1
# if n == 0:
#     print('고무오리야 사랑해')
# else:
#     print('힝구')

# 대칭 차집합
# i,u = map(int, input().split())
# a = map(int, input().split())
# b = map(int, input().split())
# set1 = set(a)
# set2 = set(b)
# x = (set1 - set2)
# y = (set2 - set1)
# c = len(x)
# d = len(y)
# print(c+d)

# 나머지
# lst = []
# for i in range(1, 11):
#     a = int(input())
#     i = a%42
#     lst.append(i)
#     result = list(set(lst))
# print(len(result))
    
# 단어 정렬
# import sys
# lst = []
# for i in range(int(sys.stdin.readline())):
#     lst.append(sys.stdin.readline().strip())
# lst_set = list(set(lst))
# lst_set.sort()
# print(*sorted(lst_set, key=len),sep='\n')

# 절댓값 힙
# import heapq
# import sys
# heap = []
# for i in range(int(sys.stdin.readline())):
#     a = int(sys.stdin.readline())
#     if a != 0:
#         heapq.heappush(heap, (abs(a), a))
#     else:
#         if heap:
#             print(heapq.heappop(heap)[1])
#         else:
#             print(0)
    