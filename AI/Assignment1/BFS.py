
graph = {
  '0' : ['1','2'],
  '1' : ['2','3'],
  '2' : ['4'],
  '3' : ['4'],
  '4' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '0')

'''
output:
Following is the Breadth-First Search
0 1 2 3 4 
'''
