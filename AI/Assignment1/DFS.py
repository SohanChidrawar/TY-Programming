graph = {
    '0' : set(['1','2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Add the starting node to visited set
    visited.add(start)

    print(start, end=" ")

    # Recursively visit all the unvisited adjacent nodes of the current node
    for next in graph[start] - visited:
        dfs(graph, next, visited)

    # Return the visited set after all nodes have been visited
    return visited

print("Following is sequence of dfs: ")
dfs(graph,'1')


'''
Following is sequence of dfs: 
1 3 0 2 4 
'''
