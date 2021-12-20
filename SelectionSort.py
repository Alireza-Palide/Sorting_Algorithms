
def SelectionSort(Array):
    #i = 0
    ALen = len(Array)
    for SNum in range(ALen-1):
        for item in range(SNum+1, ALen):
            if Array[item] < Array[SNum]:
                Array[item], Array[SNum] = Array[SNum] ,Array[item]
               #i +=1
    #print(i)
    return Array




Array = [10, 8, 12, -5, 0 , 7, 6, 2, 18, -6, -85, -7, 4, 11, 10, 5, 0, 17, -8, 1, 6, -2, 3, -17, -9,
15, 4, 57, 98, 52, 102, 21, 4, -6, -65, 102, 17, 24, -3, -57, 5, 87, -68, -5, -21, 35]


#print(sorted(Array))
print(SelectionSort(Array))   
     
    



 