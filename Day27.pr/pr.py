# 이상한 곱셈
# a, b = input().split()
# a_lst = list(map(int, a))
# b_lst = list(map(int, b))
# print(sum(a_lst)*sum(b_lst))

# 별 찍기 -1
# a = int(input())
# for i in range(1, a+1):
#     print('*'*i)

# 구구단
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i} ')

# 나는 요리사다
# lst = []
# for i in range(5):
#     a = list(map(int, input().split()))
#     lst.append(sum(a))
# rank = lst.index(max(lst))+1
# score = max(lst)
# print(f'{rank} {score}')

# 직사각형 네개의 합집합의 면적 구하기
# matrix = [[0] * 100 for _ in range(100 + 1)]
# cnt = 0
# for i in range(4):
#     x, y, x1, y1 = map(int, input().split())
#     for i in range(x, x1):
#         for j in range(y, y1):
#             if matrix[i][j] == 0:
#                 matrix[i][j] += 1
#                 cnt += 1
# print(cnt)
    
