# 공 1547
# ball = 1  # 처음에 공을 1번에 넣는다
# for i in range(int(input())):
#     a, b = map(int, input().split())
#     if a == ball: # a번호가 1번이면
#         ball = b 
#     elif b == ball: # b 번호가 1번이면
#         ball = a
# print(ball)

# 콘테스트
# Y = []           # 빈 리스트 2개를 생성
# K = []
# for i in range(10):     # Y대학 점수까지만 Y리스트에 더한다
#     Y.append(int(input()))
# for j in range(10):     # 나머지 K대학 점수를 K리스트에 더한다
#     K.append(int(input()))
# Y.sort()       # 값을 작은 ~ 큰 숫자 순으로 정렬
# K.sort()
# print(sum(Y[7:]), sum(K[7:]))  # 큰 수 3개를 더하여 결과 출력

# 오르막길
# n = int(input())
# road = list(map(int, input().split()))
# h = 0
# lst = []
# for i in range(n-1):  # n-1이 아닌 n을 넣으면 아래 [i+1] 조건에 부합하지 않음
#     if road[i] < road[i+1]: # 오르막길로 시작한다면
#         h += (road[i+1] - road[i])
#         lst.append(h)
#     else:
#         h = 0
#         lst.append(h)

# print(max(lst))

# 단어 나누기
# a = input()
# lst = []
# for i in range(1, len(a)):       # 모든 경우의 수를 구한다
#     for j in range(i+1, len(a)):
#         first = a[:i][::-1]   # m
#         second = a[i:j][::-1] # o
#         third = a[j:][::-1] # letib 
#         lst.append(first + second + third) # 글자수를 유지하며 반복한 모든 수를 더한다
# lst.sort()
# print(lst[0]) # 정렬 시 정답이 알파벳 순서상 첫번째로 나오기 때문에 [0]을 통해 출력