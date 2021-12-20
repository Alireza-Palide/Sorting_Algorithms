
def InsertionSort(array):

    for Item in range(1, len(array)):
        SelectedNum = array[Item]
        i = Item
        while i > 0 and array[i-1] > SelectedNum:
            array[i] = array[i-1]
            i -= 1
        array[i] = SelectedNum
    return array



Array = [10, 8, 12, -5, 0 , 7, 6, 2, 18, -6, -85, -7, 4, 11, 10, 5, 0, 17, -8, 1, 6, -2, 3, -17, -9,
15, 4, 57, 98, 52, 102, 21, 4, -6, -65, 102, 17, 24, -3, -57, 5, 87, -68, -5, -21, 35]

#print(sorted(Array))
print(InsertionSort(Array))

  
