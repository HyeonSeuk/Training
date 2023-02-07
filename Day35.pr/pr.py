# 막대기 17608
# import sys
# input = sys.stdin.readline # 시간초과 나서 방지용

# stack = [] # 빈 스택 생성
# cnt = 0 # 개수를 셀 카운트
# number = 0 # 비교를 위한 변수
# a = int(input()) # 반복 개수 선언을 위한 변수 생성
# for i in range(a):
#     stack.append(int(input())) # 빈 스택에 넣어준다

# for j in reversed(stack): # 오른쪽을 기준으로 계산해야 하므로 뒤집는다
#     if number < j: # 값이 크다면 오른쪽에서 보인다는 뜻
#         number = j 
#         cnt += 1  # 보이는 개수를 카운트
# print(cnt)


# 덩치 7568
# n = int(input())
# lst = []
# for t in range(n):
#     lst.append(list(map(int, input().split())))
    
# for i in range(n):
#     rank = 1 # 1등은 정해져 있으니 더하는 방식으로 가기 위해 카운트 초기 값을 1로 지정
#     for j in range(n):
#         if (lst[i][0] < lst[j][0]) and (lst[i][1] < lst[j][1]): # 키와 몸무게가 적을수록 더한다.
#             rank += 1 # 2등은 서로 몸무게 키가 비슷하면서 달라 유지되고 5등은 인원수 만큼 +1
#     print(rank, end=' ')


# 킹 1063
# directions = {
#     'R': (0,1),    # 8방향 
#     'L': (0, -1),
#     'B': (1, 0),
#     'T': (-1, 0),
#     'RT': (-1, 1),
#     'LT':(-1, -1),
#     'RB': (1, 1),
#     'LB': (1, -1)
# }

# k, s, n = input().split()

# kx, ky = 8 - int(k[1]), ord(k[0]) - 65 # 아스키 코드로 변환 후 좌표 생성
# sx, sy = 8 - int(s[1]), ord(s[0]) - 65
# # print(kx, ky)
# # print(sx, sy)

# for _ in range(int(n)):
#     d = input().strip()
#     dx, dy = directions[d] # 방향 꺼내서 쓰기
#     print(dx, dy)
#     if not (0 <= kx + dx < 8 and 0 <= ky +dy < 8 ): # 범위 지정
#         continue
#     kx += dx
#     ky += dy
#     if (kx, ky) == (sx, sy):
#         if not (0 <= sx + dx < 8 and 0 <= sy + dy < 8):
#             kx -= dx
#             ky -= dy
#             continue
#         sx += dx
#         sy += dy

# print(chr(ord('A')+ky)+str(8-kx))
# print(chr(ord('A')+sy)+str(8-sx))