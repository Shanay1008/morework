import heapq

n = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
graph = [[] for i in range(n)]

for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Start vertex: "))
visited = [False] * n
pq = [(0, start, -1)]
cost = 0

while pq:
    w, u, parent = heapq.heappop(pq)

    if visited[u]:
        continue

    visited[u] = True
    cost += w

    if parent != -1:
        print("Selected edge:", parent, "-", u, "Weight:", w)

    for v, weight in graph[u]:
        if not visited[v]:
            heapq.heappush(pq, (weight, v, u))

print("Total MST cost:", cost)


    

# 4
# 5
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4
# 0

# Selected edge: 0 - 3 Weight: 5
# Selected edge: 3 - 2 Weight: 4
# Selected edge: 0 - 1 Weight: 10
# Total MST cost: 19