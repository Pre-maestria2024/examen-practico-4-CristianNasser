from queue import Queue
from collections import defaultdict

def main():
    n, k = map(int, input().split())
    adj = defaultdict(list)
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find the depth and parent of each node
    depth = [0] * n
    parent = [-1] * n
    visited = [False] * n
    q = Queue()
    q.put(0)
    visited[0] = True
    
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                parent[v] = u
                q.put(v)
    
    # To keep track of used nodes
    used = [False] * n
    groups = 0
    
    # Process nodes in order of depth
    nodes_by_depth = sorted(range(n), key=lambda x: -depth[x])
    
    for u in nodes_by_depth:
        if not used[u]:
            # Try to form a group starting at u
            count = 0
            current = u
            while count < k and current != -1 and not used[current]:
                used[current] = True
                count += 1
                # Move to the parent node
                current = parent[current]
            if count == k:
                groups += 1
    
    print(groups)

if __name__ == '__main__':
    main()
