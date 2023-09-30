graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

m = 3
color = [-1] * len(graph)

def isSafe(node, graph, color, c):
    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

def graphColoringUtil(graph, m, node, color):
    if node == len(graph):
        for c in color:
            print(c, end=" ")
        print()
        return
    for c in range(m):
        if isSafe(node, graph, color, c):
            color[node] = c
            graphColoringUtil(graph, m, node + 1, color)
            color[node] = -1

graphColoringUtil(graph, m, 0, color)
