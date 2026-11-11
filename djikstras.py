import heapq

n = int(input("Number of vertices: "))
e = int(input("Number of edges: "))
graph = [[] for i in range(n)]

for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Source vertex: "))
dist = [float('inf')] * n
dist[start] = 0

paths = [[] for i in range(n)]
paths[start] = [start]

pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in graph[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            paths[v] = paths[u] + [v]
            heapq.heappush(pq, (dist[v], v))

for i in range(n):
    print("Vertex:", i, "Distance:", dist[i], "Path:", paths[i])


# 4
# 4
# 0 1 1
# 0 2 4
# 1 2 2
# 2 3 1
# 0
    
# Vertex: 0 Distance: 0 Path: [0]
# Vertex: 1 Distance: 1 Path: [0, 1]
# Vertex: 2 Distance: 3 Path: [0, 1, 2]
# Vertex: 3 Distance: 4 Path: [0, 1, 2, 3]