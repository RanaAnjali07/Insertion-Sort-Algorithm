
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
             
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
    
        array[j + 1] = key


data = [15,25,20,30,21,17]
insertionSort(data)
print('Sorted the given Array in Ascending Order:')
print(data)
