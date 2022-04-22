'''

--------------------------------
    Sorting Algorithms
--------------------------------

Author: Javier Martinez (somexav)
Date: 21/04/2022
    Algortihms (Intern Sorting):
                1.Insertion Sort
                2.Selection Sort
                3.Bubble Sort
'''
#-----------------------------------------------
#------------Algorithms-------------------------
#-----------------------------------------------

def InsertionSort(lista):
    for i in range(len(lista)):
        index = lista[i] 
        j = i-1 
        while(j >= 0 and lista[j] > index):
            lista[j + 1] = lista[j] 
            j -=1
        lista[j+1] = index
    return lista

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


#-----------------------------------------------
#------------------MENU-------------------------
#-----------------------------------------------
import random
option = 0
while(option !=3):
    print('******************************************')
    print('******************MENU********************')
    print('******************************************')
    print('Options:')
    print('1) If you want type your numbers:')
    print('2) Random Numbers (-999 to 999)')
    print('3) Exit')
    print('******************************************')
    
    option = int(input('Chosee yor option: '))
    
    
    if (option==1):
        n = int(input('Length of list: '))
        print('Enter your numbers:')
        list = [int(input())for i in range(int(n))]
        print('Your list: ',list)
    
    elif (option ==2):
        n = int(input('Length of list: '))
        list = [random.randint(-999, 999) for i in range(n)]
        print('Your list: ',list)
    elif (option == 3):
        print('See you!')
        break
    else: print('Error')
    
    print('******************************************')
    print('Choose the algorithm for Sort the list')
    print('1) Insertion Sort')
    print('2) Selection Sort')
    print('3) Bubble Sort')
    print('******************************************')
    
    method = int(input('Method: '))
    
    if (method == 1):
        print('Insertion Sort')
        list = InsertionSort(list)
        print('Your sorted list: ', list)
    
    elif (method ==2):
        print('Selection Sort')
        list = SelectionSort(list)
        print('Your sorted list: ', list)
        
    elif (method == 3):
        print('Bubble Sort')
        list = BubbleSort_Optimized(list)
        print('Your sorted list: ', list)
    else: 
        print('Error')
        break

