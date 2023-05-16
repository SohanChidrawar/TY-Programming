A=[64,66,12,9,56]

#Tranverse through all element
for i in range(len(A)):
    min=i
    for j in range(i+1,len(A)):
        if A[min] > A[j]:
            min = j

    #swap the element
    A[i],A[min] = A[min],A[i]

print("Sorted Array")
for i in range(len(A)):
    print(A[i], end=' ')
    
'''
Output: 
Sorted Array
9 12 56 64 66 
'''

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Input the array size and elements
size = int(input("Enter the size of the array: "))
elements = []
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    elements.append(element)

# Call the selection sort function and print the sorted array
sorted_array = selection_sort(elements)
print("Sorted array:", sorted_array)


'''
Output:

Enter the size of the array: 5
Enter element 1: 64
Enter element 2: 66
Enter element 3: 12
Enter element 4: 9
Enter element 5: 34
Sorted array: [9, 12, 34, 64, 66]

Enter the size of the array: 3
Enter element 1: 4
Enter element 2: 1
Enter element 3: 3
Sorted array: [1, 3, 4]
'''
