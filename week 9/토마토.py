import sys

input = sys.stdin.readline

from collections import deque
# collections 모듈 deque 설명 :: https://excelsior-cjh.tistory.com/96

M, N, H = map(int, input().split()) # M 가로, N 세로, H 쌓아올린 상자의 수

graph = []
queue = deque([])

tomato = [list(map(int, input().split())) for _ in range(N)] # 2차원 리스트로 토마토 넣어두기

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append([i, j, k])
    graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while(queue):
    x, y, z = queue.popleft()
    for i in range(6):
        # i == 0일 때 [-1, 0, 0] 좌
        # i == 1일 떄 [1, 0, 0] 우
        # i == 2일 떄 [0, 1, 0] 하
        # i == 3일 떄 [0, -1, 0] 상
        # i == 4일 떄 [0, 0, 1] 아랫집
        # i == 5일 떄 [0, 0, -1] 윗집
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and graph[nx][ny][nz] == 0:
                queue.append([dx, dy, dz])
                graph[dx][dy][dz] = graph[x][y][z] + 1

day = 0

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day - 1) 