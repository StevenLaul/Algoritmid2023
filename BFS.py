from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Lisa see rida, kui graaf on suunatud

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Graafi näide
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

print("BFS algoritmi tulemus:")
graph.bfs(1)