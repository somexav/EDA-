'''
Author: Javier Martinez (somexav)
Date: 20/04/2022
--------------------------------
Code of BubbleSort_V2
--------------------------------
'''


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''--------------------------------
Code of BubbleSort_V2 Optimized
--------------------------------
'''



def bubbleSort_Optimized(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        print(i)
        swapped = False
        # Last i elements are already
        #  in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            print('Finished with i = %d'%(i))
            break
    return arr


# Driver code to test above
arr = [10,9,8,7,6,5,4,3,2,1,0]

print(bubbleSort_Optimized(arr))
