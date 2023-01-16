# 평균 점수

# n = 0
# for i in range(5):
#     numbers = int(input())
#     if numbers < 40:
#         numbers = 40
#     n += numbers
# print(n//5)

# X보다 작은 수

# a, b = list(map(int, input().split()))
# numbers = list(map(int, input().split()))

# for i in numbers:
#     if b > i:
#         print(i, end=' ')

# 주사위 세개

# a, b, c = list(map(int, input().split()))
# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# elif a != b != c:
#     print(max(a,b,c)*100)

# 0 = not cute / 1 = cute

# p = int(input())
# yes = 0
# no = 0
# for i in range(p):
#     a = int(input())
#     if a == 0:
#         no += 1
#     elif a == 1:
#         yes += 1
# if no > yes:
#     print('Junhee is not cute!')
# else:
#     print('Junhee is cute!')

# 점수계산

# score = int(input())
# numbers = list(map(int, input().split()))
# sum = 0
# count = 0
# for i in range(score):
#     if numbers[i] == 1:
#         count += 1
#     else:
#         count = 0
#     sum += count
# print(sum) 