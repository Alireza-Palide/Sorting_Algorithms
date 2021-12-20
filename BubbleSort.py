a =2
def BubbleSort(array):
    #i = 0
    ALen = len(array)
    for Round in range(ALen):
        IsChanged = False
        for Item in range(ALen - (Round+1)):
            if array[Item] > array[Item+1]:
                IsChanged = True
                array[Item], array[Item+1] = array[Item+1], array[Item]
                #i +=1
        if IsChanged == False:
            #print(i)
            return array
    #print(i)
    return array



Array = [10, 8, 12, -5, 0 , 7, 6, 2, 18, -6, -85, -7, 4, 11, 10, 5, 0, 17, -8, 1, 6, -2, 3, -17, -9,
15, 4, 57, 98, 52, 102, 21, 4, -6, -65, 102, 17, 24, -3, -57, 5, 87, -68, -5, -21, 35]

#print(sorted(Array))
print(BubbleSort(Array))