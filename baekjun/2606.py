def dfs(net,start_node,v):
  v[start_node] = True
  count = 1
  for neighbor in net[start_node]:  # 현재 노드와 연결된 모든 이웃 노드 확인
        if not v[neighbor]:  # 아직 방문하지 않은 이웃 노드라면
            count += dfs(net, neighbor, v)
  return count
com = int(input())
t = int(input())
net = [[] for _ in range(com)]
v = [False]*com
for i in range(t):
  com1,com2 = map(int,input().split())
  net[com1-1].append(com2-1)
  net[com2-1].append(com1-1)
print(dfs(net,0,v)-1)


