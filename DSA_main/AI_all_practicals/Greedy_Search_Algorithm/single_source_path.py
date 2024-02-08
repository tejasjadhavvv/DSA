import heapq


def greedy_search(graph, start):
    # Create a priority queue to store the vertices
    
    # This is actually the intial value of the queue varible having priority  queue which creates the priority based on the minimum distance
    queue = [(0, start)]
    # Create a dictionary to store the shortest distances
    distances = {vertex: float('inf') for vertex in graph}
    # Set the distance from the start vertex to itself as 0
    distances[start] = 0

    while queue:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(queue)

        # Ignore if the distance to the current vertex is greater than the stored distance
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        
        # this code of the line are used for the iterate throught the vertex of the graph and calculating the desired distance from the source node
        
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add the neighbor to the priority queue
                heapq.heappush(queue, (distance, neighbor))

    return distances
    
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 3},
    'C': {'D': 1},
    'D': {'A': 1}
}

start_vertex = 'A'

shortest_distances = greedy_search(graph, start_vertex)
print(shortest_distances)