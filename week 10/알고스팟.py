# 백준 알고리즘 저지 1261번
# https://www.acmicpc.net/problem/1261

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
room = []

for _ in range(m):
    room.append(input())

dist = [[-1]*n for _ in range(m)]
dist[0][0] = 0

que = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que.append([0, 0])

while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if dist[nx][ny] == -1:
                if room[nx][ny] == '0':
                    que.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif room[nx][ny] == '1':
                    que.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1


print(dist[m-1][n-1])