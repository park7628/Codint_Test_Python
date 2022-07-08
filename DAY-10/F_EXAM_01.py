def DFS(x,y):
    dx = [-1, 0, 1, 0] # 4가지 방향 정의
    dy = [0, 1, 0, -1]
    for i in range(4): # 상하좌우 검사
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0: # 이어저있는 얼음 발견
            graph[nx][ny]=1 #1로 바꿔줌으로 다시 탐색되지 않도록 함
            DFS(nx,ny) # DFS 재귀 호출

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
    # 현재 위치에서 DFS 수행
        if graph[i][j] == 0:
            graph[i][j] = 1 #초기 값을 바꿔줌
            DFS(i, j)
            result += 1 #얼음의 갯수 증가
            
print(result) # 정답 출력
