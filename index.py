#assignment deisgn and analysis of algorithm
#Bubble sort 

import time;

# def bubbleSort(arr):
#     n = len(arr)
    

#     for i in range(n):
#         swapped = False


#         for j in range(0, n-i-1):


#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if (swapped == False):
#             break


# if __name__ == "__main__":
#     arr = [64, 34, 25, 12, 22, 11, 90] #worst case 
#     #arr = [99, 88, 73, 65, 61, 76 , 34] #avrage case 
#     #arr = [10, 20 , 30, 40, 50, 60, 70] #best case 

#     bubbleSort(arr)

#     print("Sorted array:")
#     for i in range(len(arr)):
#         print("%d" % arr[i], end=" ")
# secounds = time.time()
# def convert_seconds(seconds):
   
#     remaining_seconds = seconds % 60
    
#     return f" {remaining_seconds} seconds"

# programtime = convert_seconds(secounds)
# print('\n\n','bubble sort run in :- ',programtime)


                    #seletion sort 



# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
      
        
#         min_idx = i
        
        
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
              
                
#                 min_idx = j
        
       
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# def print_array(arr):
#     for val in arr:
#         print(val, end=" ")
#     print()

# if __name__ == "__main__":
#     arr = [64, 25, 12, 22, 11] #worst case
#      #arr = [99, 88, 73, 65, 61, 76 , 34] #avrage case 
#      #arr = [10, 20 , 30, 40, 50, 60, 70] #best case 
    
#     print("Original array: ", end="")
#     print_array(arr)
    
#     selection_sort(arr)
    
#     print("Sorted array: ", end="")
#     print_array(arr)

# secounds = time.time()
# def convert_seconds(seconds):
   
#     remaining_seconds = seconds % 60
    
#     return f" {remaining_seconds} seconds"

# programtime = convert_seconds(secounds)
# print('\n\n','Selection sort run in :- ',programtime)



#             merge sort

# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid

#     # Create temp arrays
#     L = [0] * n1
#     R = [0] * n2

   
#     for i in range(n1):
#         L[i] = arr[left + i]
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]

#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = left  # Initial index of merged subarray

   
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

  
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

  
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def merge_sort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2

#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)
#         merge(arr, left, mid, right)

# def print_list(arr):
#     for i in arr:
#         print(i, end=" ")
#     print()

# # Driver code
# if __name__ == "__main__":
#     arr = [64, 25, 12, 22, 11] #worst case
#     #arr = [99, 88, 73, 65, 61, 76 , 34] #avrage case 
#     #arr = [10, 20 , 30, 40, 50, 60, 70] #best case 
#     print("Given array is")
#     print_list(arr)

#     merge_sort(arr, 0, len(arr) - 1)

#     print("\nSorted array is")
#     print_list(arr)
# secounds = time.time()
# def convert_seconds(seconds):
   
#     remaining_seconds = seconds % 60
    
#     return f" {remaining_seconds} seconds"

# programtime = convert_seconds(secounds)
# print('\n\n','merge sort run in :- ',programtime)


                #quick sort

# def partition(arr, low, high):
    
#     # Choose the pivot
#     pivot = arr[high]
    
   
#     i = low - 1
    
   
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             swap(arr, i, j)
   
#     swap(arr, i + 1, high)
#     return i + 1


# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]


# def quickSort(arr, low, high):
#     if low < high:
        
#         # pi is the partition return index of pivot
#         pi = partition(arr, low, high)
        
#         # Recursion calls for smaller elements
#         # and greater or equals elements
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

# # Main driver code
# if __name__ == "__main__":
#     arr = [64, 25, 12, 22, 11] #worst case
#     #arr = [99, 88, 73, 65, 61, 76 , 34] #avrage case 
#     #arr = [10, 20 , 30, 40, 50, 60, 70] #best case 
#     n = len(arr)

#     quickSort(arr, 0, n - 1)
    
#     for val in arr:
#         print(val, end=" ") 

# secounds = time.time()
# def convert_seconds(seconds):
   
#     remaining_seconds = seconds % 60
    
#     return f" {remaining_seconds} seconds"

# programtime = convert_seconds(secounds)
# print('\n\n','quick sort run in :- ',programtime)
