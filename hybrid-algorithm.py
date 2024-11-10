from collections import deque

def hybrid_bfs_dfs(graph, start):
    visited = set()
    
    # BFS Queue and DFS Stack
    queue = deque([start])   # BFS queue
    stack = []               # DFS stack
    
    while queue or stack:
        if queue:
            # BFS Step
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(f"BFS visiting {node}")
                
                # Switch to DFS if deep subgraph detected (arbitrary heuristic)
                if len(graph[node]) > 4:
                    print(f"Switching to DFS for node {node}")
                    stack.append(node)
                else:
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        
        if stack:
            # DFS Step
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(f"DFS visiting {node}")
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# Running the hybrid traversal
hybrid_bfs_dfs(graph, 'A')
