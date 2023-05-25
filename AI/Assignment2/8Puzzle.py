#used to create a copy of puzzle state
import copy  

# initial = [[1,2,3],[-1,4,6],[7,5,8]]
# final = [[1,2,3],[4,5,6],[7,8,-1]]

# Function to find heuristic cost
# Heuristic function counts the number of tiles that are not in their correct positions in comparison to the final state.
def gn(state, finalstate):
    count = 0
    for i in range(3):
        for j in range(3):
            if(state[i][j]!=-1):
                if(state[i][j] != finalstate[i][j]):
                    count+=1

    return count

# Function of find position of blank tile
def findposofblank(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j] == -1):
                return [i,j]
'''
'retarr' = 2D list representing current state of puzzle
'pos' = is a list contaning the rows and column indices of a particular element in the puzzle that need
        to be swapped with its adjacent element
'retarr[pos[0]][pos[1]]' = represent value of current element
'retarr[pos[0]][pos[1]-1]' =  represents the value of the adjacent element on the left side.
'''
def move_left(state,pos):
    if(pos[1]==0):               # Check if already at the leftmost column
        return None
    
    retarr = copy.deepcopy(state)
    retarr[pos[0]][pos[1]],retarr[pos[0]][pos[1]-1] = retarr[pos[0]][pos[1]-1],retarr[pos[0]][pos[1]]
    return retarr

def move_up(state,pos):
    if(pos[0]==0):              # Check if already at the top row
        return None
    
    retarr = copy.deepcopy(state)
    retarr[pos[0]][pos[1]],retarr[pos[0]-1][pos[1]] = retarr[pos[0]-1][pos[1]],retarr[pos[0]][pos[1]]
    return retarr

def move_right(state,pos):
    if(pos[1]==2):              # Check if already at the rightmost column
        return None
    
    retarr = copy.deepcopy(state)
    retarr[pos[0]][pos[1]],retarr[pos[0]][pos[1]+1] = retarr[pos[0]][pos[1]+1],retarr[pos[0]][pos[1]]
    return retarr

def move_down(state,pos):
    if(pos[0]==2):              # Check if already at the bottom row
        return None
    
    retarr = copy.deepcopy(state)
    retarr[pos[0]][pos[1]],retarr[pos[0]+1][pos[1]] = retarr[pos[0]+1][pos[1]],retarr[pos[0]][pos[1]]
    return retarr

# Used to print the steps and states of puzzle
def printMatrix(matricarray):
    print("")
    counter = 1
    for matrix in matricarray:
        print('Step {}'.format(counter))
        for row in matrix:
            print(row)
        counter+=1
        print("")

# Function for A* algo
# It uses a heuristic function to estimate the cost of reaching the final state from the current state.
# The function explores different moves and selects the one with the minimum estimated cost until the final state is reached.
def eightPuzzle(initalstate,finalstate):
    hn = 0
    explored=[]         # it keep track of state that have already been visited during search process   

    while(True):
        explored.append(initalstate)
        if(initalstate == finalstate):
            break

        hn += 1

        left = move_left(initalstate, findposofblank(initalstate))
        right = move_right(initalstate, findposofblank(initalstate))
        down = move_down(initalstate, findposofblank(initalstate))
        up = move_up(initalstate, findposofblank(initalstate))

        fnl =1000
        fnr = 1000
        fnd=1000
        fnu = 1000

        if(left!=None):                      # check if move to left is valid or not
            fnl = hn + gn(left, finalstate)

        if(right!=None):                     # check if move to right is valid or not
            fnr = hn +gn(right,finalstate)

        if(down!=None):                      # check if move to down is valid or not
            fnd = hn+gn(down, finalstate)

        if(up!=None):                       # check if move to up is valid or not
            fnu = hn+gn(up,finalstate)

        minfn = min(fnl,fnr,fnd,fnu)

        if((fnl==minfn) and (left not in explored)):
            initalstate = left

        elif ((fnr==minfn) and (right not in explored)):
            initalstate = right

        elif((fnd==minfn) and (down not in explored)):
            initalstate = down

        else:
            initialstate = up

    printMatrix(explored)

def main():
    while(True):
        ch = int(input("Press 1 to continue and 0 to exit: "))
        if(not ch):
            break

        start = [] 
        print('Start State: \n')
        # create a 2D list representing staring state of puzzle
        for i in range(3):          # iterate over row of puzzle
            arr = [] 
            for j in range(3):      # iterate over column of puzzle
                a = int(input("Enter element at {},{} :".format(i,j)))
                arr.append(a)
            start.append(arr)

        final=[]
        print('Final state: \n')
        # create a 2D list representing final state of puzzle
        for i in range(3):
            arr =[]
            for j in range(3):
                a = int(input('Enter Element at {},{}:'.format(i,j)))
                arr.append(a)
            final.append(arr)

        eightPuzzle(start,final)

main() 

'''
Output:

Press 1 to continue and 0 to exit: 1
Start State: 
Enter element at 0,0 :1
Enter element at 0,1 :2
Enter element at 0,2 :3
Enter element at 1,0 :-1
Enter element at 1,1 :4
Enter element at 1,2 :6
Enter element at 2,0 :7
Enter element at 2,1 :5
Enter element at 2,2 :8
Final state: 

Enter Element at 0,0:1
Enter Element at 0,1:2
Enter Element at 0,2:3
Enter Element at 1,0:4
Enter Element at 1,1:5
Enter Element at 1,2:6
Enter Element at 2,0:7
Enter Element at 2,1:8
Enter Element at 2,2:-1

Step 1
[1, 2, 3]
[-1, 4, 6]
[7, 5, 8]

Step 2
[1, 2, 3]
[4, -1, 6]
[7, 5, 8]

Step 3
[1, 2, 3]
[4, 5, 6]
[7, -1, 8]

Step 4
[1, 2, 3]
[4, 5, 6]
[7, 8, -1]

Press 1 to continue and 0 to exit: 0
'''
