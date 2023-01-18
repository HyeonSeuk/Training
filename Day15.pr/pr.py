# 시험 성적
# score = int(input())
# if 100 >= score and 90 <= score:
#     print('A')
# elif 89 >= score and 80 <= score:
#     print('B')
# elif 79 >= score and 70 <= score:
#     print('C')
# elif 69 >= score and 60 <= score:
#     print('D')
# else:
#     print('F')


# 단어 뒤집기
# T = int(input())

# for t in range(1, T+1):
#     a = input().split(' ')
#     for i in a:
#         print(i[::-1], end=' ')


# 열 개씩 끊어 출력하기
# a = input()
# for i in range(0, len(a), 10):
#     print(a[i:i+10])


# 나무 조각
# a = list(map(int, input().split()))
# numbers = [1, 2, 3, 4, 5]
# while a != numbers:
#     for i in range(4):
#         if a[i] > a[i+1]:
#             temp = a[i]
#             a[i] = a[i+1]
#             a[i+1] = temp
#             print(*a)