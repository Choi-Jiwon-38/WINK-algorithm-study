# 백준 알고리즘 저지 16929번
# https://www.acmicpc.net/problem/16929


N, M = map(int, input().split()) # N, M을 공백을 기준으로 구분 후, 입력받음

board = [] # 2차원 빈 리스트 생성
for i in range(N): # 주어진 정보를 board에 담음
    board.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cycle = False

def dfs(x, y, cX, cY, count, color):
    global cycle
    global result
    if cycle:
        return
    
    visited[cX][cY] = True # 방문한 지점 표시
    if x == cX and y == cY and count >= 4:
        cycle = True
        return
    
    for i in range(4): # 네 방향 모두 조사
        nx = cX + dx[i]
        ny = cX + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and color == board[nx][ny]:
                dfs(x, y, nx, ny, count+1, color)
            elif nx == x and ny == y and count >= 4:
                dfs(x, y, nx, ny, count, color)
    return

# 현재 위치에서 DFS를 이용하여 YES, NO 판별

for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        dfs(i, j, i, j, 1, board[i][j])


if cycle:
    print('Yes')
else:
    print('No')