'''
Author: Javier Martinez (somexav)
Date: 20/04/2022
--------------------------------
Code of BubbleSort
--------------------------------
'''
def BubbleSort(list):
    n = len(list)
    for i in range(n,0,-1):    
        for j in range(i-1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list
#list = [0.1,28,45,10,24,3,60,321,1,0]

#print(BubbleSort(list))

'''
--------------------------------
Code of BubbleSort Optimized
--------------------------------
'''
def BubbleSort_Optimized(list):
    #Lenght of the list/array
    n = len(list)
    for i in range(n,0,-1): 
        completed = False   
        for j in range(i-1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                completed = True
        if completed == False:
            print("Completed with i = %d"%(i))
            break
    return list       

    
list = [0,1,2,4,5]

print(BubbleSort_Optimized(list))



