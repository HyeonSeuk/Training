# 오븐 시계
# a, b = map(int, input().split())
# c = int(input())
# a += c // 60
# b += c % 60

# if b >= 60:
#     a += 1
#     b -= 60

# if a >= 24:
#     a-=24
    
# print(a, b)

# 블랙잭
# a, b = map(int, input().split())
# card = list(map(int, input().split()))
# lst = []
# for i in range(0, a-2):
#     for j in range(i+1, a-1):
#         for k in range(j+1, a):
#             if card[i] + card[j] + card[k] <= b:
#                 lst.append(card[i] + card[j] + card[k])
# print(max(lst))

# 점수 집계
# for i in range(int(input())):
#     lst = []
#     a = map(int,input().split())
#     for i in a:
#         lst.append(i)
#         lst.sort()
    
#     x = lst[3] - lst[1]

#     if x < 4:
#         print(sum(lst[1:4]))
#     else:
#         print('KIN')

# 가장 큰 금민수
# n = int(input())
# cnt = 0

# for i in range(4,int(n)+1):
#     s = str(i)
#     a = s.count('4')+s.count('7')
#     if a == len(s): #4와 7로만 이루어진 숫자를 찾는다.
#         cnt = i #4와 7로만 이루어져 있어야 하기 때문에 4의 개수와 7의 개수를 더한 값이 숫자의 자릿수와 같아야 한다.

# print(cnt)

# 영화 감독 숌
# n = int(input())
# cnt = 0
# six = 666
 
# while True:
#     if '666' in str(six):
#         cnt += 1
 
#     if cnt == n:
#         print(six)
#         break
#     six += 1
 
