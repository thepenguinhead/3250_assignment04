from graphs_jjarek import sp

graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 3: 7, 8: 2, 5: 4},
    3: {2: 7, 4: 9, 5: 14},
    4: {3: 9, 5: 10},
    5: {2: 4, 3: 14, 4: 10, 6: 2},
    6: {5: 2, 7: 1, 8: 6},
    7: {0: 8, 1: 11, 6: 1, 8: 7},
    8: {2: 2, 6: 6, 7: 7}
}

# Source vertex
source = 0

# Call Dijkstra's algorithm
dist, path = sp.dijkstra(graph, source)

# Output results
print(f"Shortest distances from {source}: {dist}")
print(f"Paths: {path}")