''' graph = {'A':['B', 'E', 'C'],
         'B':['A', 'D', 'E'],
         'D':['B', 'E'],
         'E':['A', 'D', 'B'],
         'C':['A', 'F', 'G'],      
         'F':['C'],
         'G':['C']
         }
'''
'''
graph = {
    '0' : ['1','2','3'],
    '1' : ['0'],
    '2' : ['3','4'],
    '3' : ['0','2'],
    '4' : ['2']
}
'''
graph = {
    '0' : ['1','2'],
    '1' : ['2'],
    '2' : ['3','0'],
    '3' : ['3'],
}
visited = []
stack = []
def dfs(visited, graph, start):
    # print("DFS traveral is: ")
    stack.append(start)
    visited.append(start)
    while stack:
        node = stack[-1]
        stack.pop()
        print(node, end=' ')
        
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

print('DFS traversal is: ')
dfs(visited, graph, '2')

'''
OUTPUT

DFS traversal is: 
2 0 1 3 

'''
