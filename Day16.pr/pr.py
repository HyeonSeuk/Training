# 홀수
# lst = []
# for i in range(7):
#     a = int(input())
#     if a % 2 == 1:
#         lst.append(a)
# if lst == []:
#     print(-1)
# else:
#     print(sum(lst))
#     print(min(lst))


# 더하기
# a = map(int, input().split(','))
# print(sum(a))


# 학점계산
# dict = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,

# 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,

# 'C+': 2.3, 'C0': 2.0, 'C-': 1.7,

# 'D+': 1.3, 'D0': 1.0, 'D-': 0.7,

# 'F': 0.0}
# print(dict[input()])


# 다이얼
# a = input()
# time = 0
# for i in a:
#     if i in ['A', 'B', 'C']:
#         time = time + 3
#     elif i in ['D', 'E', 'F']:
#         time = time + 4
#     elif i in ['G', 'H', 'I']:
#         time = time + 5
#     elif i in ['J', 'K', 'L']:
#         time = time + 6
#     elif i in ['M', 'N', 'O']:
#         time = time + 7
#     elif i in ['P', 'Q', 'R', 'S']:
#         time = time + 8
#     elif i in ['T', 'U', 'V']:
#         time = time + 9
#     elif i in ['W', 'X', 'Y', 'Z']:
#         time = time + 10
# print(time)


# 숫자의 개수
# n = int(input()) * int(input()) * int(input()) 
# a = str(n) 
# for i in range(10):
#     print(a.count(str(i)))

# 회사에 있는 사람
# company = {}
# for t in range(int(input())):
#     Key, Value = input().split()
#     if Value == 'enter':
#         company[Key] = True
#     else:
#         del(company[Key])

# for Key in sorted(company.keys(), reverse=True):
#     print(Key)