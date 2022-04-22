'''
Author: Javier Martinez (somexav)
Date: 20/04/2022
--------------------------------
Code of Selection Sort 
--------------------------------
'''
def SelectionSort(list):
    for i in range(len(list)): #Iterations of the algorithm
        # Find the minimum element in remaining 
        min_idx = i
        
        for j in range(i+1,len(list)):
            if (list[j] < list[min_idx]):
                min_idx = j
        # Swap the found minimum element with the first element   
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

list = [40,13,28,7,32,15,24]


print(SelectionSort(list))
        