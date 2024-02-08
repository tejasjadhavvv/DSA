# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         # Find the minimum element in the remaining unsorted part of the list
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         # Swap the minimum element with the first element of the unsorted part
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return arr


# # Test the selection_sort function
# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)





def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index= i
        for j in range (i+1 ,n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    
    return arr

arr=[12,11,15,1,0,100]
sorted_arr= selection_sort(arr)
print("The sorted list ",sorted_arr)
                
    



