# 삼각형 외우기
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c == 60:
#     print('Equilateral')
# elif (a+b+c) == 180:
#     if a == b or a == c or b == c:
#         print('Isosceles')
#     else:
#         print('Scalene')
# elif (a+b+c) != 180:
#     print('Error')

# 세탁소 사장 동혁
# money = [25, 10, 5, 1]
# for t in range(int(input())):
#     person = int(input())
#     lst = []
#     for i in money:
#         lst.append(person // i)
#         person = person % i
#     print(*lst)

# 피시방 알바
# lst = []
# person = int(input())
# want = list(map(int, input().split()))
# n = 0
# for i in range(person):
#     if want[i] in lst:
#         n += 1
#     else:
#         lst.append(want[i])
# print(n)

# 제로
# stack = []

# for t in range(int(input())):
#     a = int(input())
    
#     if a == 0:
#         stack.pop()
#     else:
#         stack.append(a)
# print(sum(stack))

# 카드 1
# queue = list(range(1, int(input())+1))

# while len(queue) > 1:
#     print(queue.pop(0), end = ' ')
#     queue.append(queue.pop(0))

# print(queue[0])

# 괄호        
# for t in range(int(input())):
#     a =input()
#     while '()' in a:
#         a = a.replace('()','')
#     if len(a) == 0: 
#         print('YES')
#     else: 
#         print('NO')