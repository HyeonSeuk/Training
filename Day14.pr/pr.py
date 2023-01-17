# 더하기
# T = int(input())

# for t in range(1, T+1):
#     int(input())
#     print(sum(map(int, input().split())))

# 네수
# a, b, c, d = input().split()
# ab = int(a+b)
# cd = int(c+d)
# print(ab + cd)

# 네 번째 점
# a, b = list(map(int, input().split()))
# c, d = list(map(int, input().split()))
# e, f = list(map(int, input().split()))

# if a == c:
#     x = e
# elif c == e:
#     x = a
# else:
#     x = c

# if b == d:
#     y = f
# elif d == f:
#     y = b
# else:
#     y = d

# print(f'{x} {y}')

# A + B -5
# while True:
#     a, b = list(map(int, input().split()))
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a+b)

# 더하기 사이클
# a = int(input())
# b = a
# cycle = 1
# while True:
#     x = b//10
#     y = b%10
#     mix = x + y
#     b = (y*10)+(mix%10)
#     if b == a:
#         break
#     else:
#         cycle += 1
# print(cycle)