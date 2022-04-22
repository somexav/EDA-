'''
Author: Javier Martinez (somexav)
Date: 20/04/2022
--------------------------------
Code of InsertionSort Descending
--------------------------------
'''
lista = [25,4,12,3,32,29,60]

def InsertionSort(lista):
    for i in range(len(lista)):
        index = lista[i] 
        j = i-1 
        while(j < 0 and lista[j] <= index):
            lista[j + 1] = lista[j] 
            j -=1
        lista[j+1] = index
    return lista

print(InsertionSort(lista))






