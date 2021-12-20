
def CountingSort(array):

    myLen = max(array)
    Count = [0] * (myLen+1)
    for Num in array:
        Count[Num] += 1

    array = []
    for Sorted_num in range(myLen+1):
        array += Count[Sorted_num]*[Sorted_num]
    
    return array


Array = [2, 8, 5, 2, 8, 2, 2, 8, 5, 5, 5, 8, 2, 5, 8, 2, 2, 5, 2, 5, 8, 8, 2, 8, 2, 5]

print (CountingSort(Array))