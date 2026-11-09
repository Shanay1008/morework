import heapq as hp
import math

n=int(input())
m=int(input())
coords=[tuple(map(float,input().split())) for i in range(n)]
adj=[[] for i in range(n)]

for i in range(m):
    p,q,w=input().split()
    p,q,w=int(p),int(q),float(w)
    adj[p].append((q,w))
    adj[q].append((p,w))

def astar(s,t,n,adj,coords):
    def h(u):
        x1,y1=coords[u]
        x2,y2=coords[t]
        return math.hypot(x1-x2,y1-y2)

    pq=[(h(s),0,s,[s])]
    g=[float('inf')]*n
    g[s]=0

    while pq:
        f,cost,u,path=hp.heappop(pq)

        if cost>g[u]:
            continue

        if u==t:
            return path,cost

        for v,w in adj[u]:
            ng=cost+w
            if ng<g[v]:
                g[v]=ng
                hp.heappush(pq,(ng+h(v),ng,v,path+[v]))

    return [],float('inf')

s,t=map(int,input().split())
path,cost=astar(s,t,n,adj,coords)

print("Path:",path)
print("Cost:",cost)