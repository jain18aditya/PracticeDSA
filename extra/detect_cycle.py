#Design a dependency-aware test scheduler and detect cycles.Design a dependency-aware test scheduler and detect cycles.
#
def detect_cycle(graph):
    states = {state: "unvisited" for state in graph }
    cycles = []
    stack = []

    def dfs(node):
        states[node] = "visiting"
        stack.append(node)
        for neighbor in graph[node]:
            if states[neighbor] == "unvisited":
                dfs(neighbor)
            elif states[neighbor] == "visiting":
                idx = stack.index(node)
                cycles.append(stack[idx:] + [neighbor])
        stack.pop()
        states[node] = "visited"

    for node in graph:
        if states[node] == "unvisited":
            dfs(node)
    return cycles

def build_graph_from_edges(edges: list[tuple]) -> dict:
    graph = {}
    for src, dst in edges:
        graph[dst].append(src)
    return graph

graph = {
    'test_setup':   [],
    'test_users':   ['test_setup'],
    'test_orders':  ['test_setup'],
    'test_billing': ['test_users', 'test_orders'],
}
print(detect_cycle(graph))

graph = {
    'test_a': ['test_b'],
    'test_b': ['test_c'],
    'test_c': ['test_a'],  # cycle back to a
}
print(detect_cycle(graph))

edges = [('a', 'b'), ('c', 'd'), ('d', 'a')]
graph = build_graph_from_edges(edges)
print(detect_cycle(graph))
