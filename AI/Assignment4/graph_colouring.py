# Number of vertices in graph
# define 4 4

def isSafe(graph,color):
    
    for i in range(4):
        for j in range(i+1,4):
            if (graph[i][j] and color[j] == color[i]):
                return False                            # if two adjacent vertices has same color it return false
    return True

def graphColouring(graph,m,i,color):
    if(i==4):
        # Base case all vertices are color
        if(isSafe(graph,color)):
            # Valid color solution find so print it
            printSolution(color)
            return True
        return False
    
    #assign each color from 1 to m
    for j in range(1,m+1):
        color[i] = j

        if graphColouring(graph,m,i+1,color):
            return True
        color[i]=0       #Backtrack
    return False

def printSolution(color):
    print('Solution exist: " " Following are the assigned color')
    for i in range(4):
        print(color[i],end=' ')

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
     
    m=3    #number of color

    color = [0  for i in range(4)]

    if(not graphColouring(graph,m,0,color)):
        print('Solution does not exist')
        
'''
Output:

Solution exist: " " Following are the assigned color
1 2 3 2 
'''
