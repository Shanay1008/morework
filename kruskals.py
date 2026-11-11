n = int(input("Number of vertices: "))
e = int(input("Number of edges: "))

edges = []
for i in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))

    
# The find() function follows these parent connections to determine whether two vertices already belong to the same group
# helping prevent cycles.

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

cost = 0

print("Sorted edges:", edges)
print("MST edges:")

for w, u, v in edges:
    a = find(u)
    b = find(v)

    print("Checking:", u, "-", v, "Weight:", w)

    if a != b:
        parent[a] = b
        cost += w
        print("Accepted:", u, "-", v)
    else:
        print("Rejected: Cycle detected")

print("Total MST cost:", cost)


    
    


# 4
# 5
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4

# Sorted edges: [(4, 2, 3), (5, 0, 3), (6, 0, 2), (10, 0, 1), (15, 1, 3)]
# MST edges:
# Checking: 2 - 3 Weight: 4
# Accepted: 2 - 3
# Checking: 0 - 3 Weight: 5
# Accepted: 0 - 3
# Checking: 0 - 2 Weight: 6
# Rejected: Cycle detected
# Checking: 0 - 1 Weight: 10
# Accepted: 0 - 1
# Checking: 1 - 3 Weight: 15
# Rejected: Cycle detected
# Total MST cost: 19