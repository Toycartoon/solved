from collections import deque

q = deque()
def bfs(_x, visited, computers):
    visited[_x] = True
    q.append(_x)
    
    while q:
        x = q.popleft()
        
        for v in range(len(computers[x])):
            if computers[x][v] == 1 and not visited[v]:
                visited[v] = True
                q.append(v)
    
    return visited

def solution(n, computers):
    ans = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            visited = bfs(i, visited, computers)
            ans += 1
    return ans
