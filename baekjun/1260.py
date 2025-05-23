from collections import deque

def dfs(graph, check, start):
    result = []
    check[start] = True
    result.append(start)
    for neighbor in graph[start]:
        if not check[neighbor]:
            result += dfs(graph, check, neighbor)
    return result

def bfs(graph, check, start):
    queue = deque([start])
    result = []
    check[start] = True
    while queue:
        v = queue.popleft()
        result.append(v)
        for neighbor in graph[v]:
            if not check[neighbor]:
                check[neighbor] = True
                queue.append(neighbor)
    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i] = sorted(graph[i])

check = [False] * (n + 1)
dfs_result = dfs(graph, check, v)

check = [False] * (n + 1)
bfs_result = bfs(graph, check, v)

print(*dfs_result)
print(*bfs_result)
