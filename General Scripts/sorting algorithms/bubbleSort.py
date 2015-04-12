__author__ = 'github.com/ramwho'

from datetime import datetime

def originalBubbleSort(numberArray):
    
    start_time = datetime.now()
    
    for i in range(0,len(numberArray)):
        for j in range(0,len(numberArray)-1):
            if(numberArray[j] > numberArray[j+1]):
                temp = numberArray[j]
                numberArray[j] = numberArray[j+1]
                numberArray[j+1] = temp
    
    stop_time = datetime.now()            
    
    return numberArray,start_time,stop_time


def modifiedBubbleSort(numberArray):
    start_time = datetime.now()
    swapped = 1
    while(swapped == 1):
        swapped = 0
        for i in range(0,len(numberArray)-1):
            #print i,numberArray,counter,isSorted
            if(numberArray[i] > numberArray[i+1]):
                temp = numberArray[i]
                numberArray[i] = numberArray[i+1]
                numberArray[i+1] = temp
                swapped = 1
                
    stop_time = datetime.now()
    return numberArray,start_time,stop_time


while(1):       
    userInput = raw_input('Enter the number array you wish to sort')
    userInput = userInput.strip()
    unsortedNumbers = [int(n) for n in userInput.split(' ')]

    origBubbleSortResult = originalBubbleSort(unsortedNumbers[:])
    modBubbleSortResult = modifiedBubbleSort(unsortedNumbers[:])

    print 'The array sorted using original bubble Sort is:' , origBubbleSortResult[0] , 'Execution time' , (origBubbleSortResult[2] - origBubbleSortResult[1])  
    print 'The array sorted using modified bubble Sort is:', modBubbleSortResult[0] ,'Execution time' , (modBubbleSortResult[2] - modBubbleSortResult[1])  

