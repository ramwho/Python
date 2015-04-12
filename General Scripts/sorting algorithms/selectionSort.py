___author___ = 'github.com/ramwho'

from datetime import datetime

def selectionSort(numberArray):
    
    start_time = datetime.now()
    smallest = 0
    
    for i in range(0,len(numberArray)-1):
        smallest = i
        for j in range(i,len(numberArray)):
            if (numberArray[j] < numberArray[smallest]):
                smallest = j
        if(smallest != i):
            temp = numberArray[i]
            numberArray[i] = numberArray[smallest]
            numberArray[smallest] = temp
    
    stop_time = datetime.now()
    
    return numberArray,start_time,stop_time




while(1):       
    userInput = raw_input('Enter the number array you wish to sort')
    userInput = userInput.strip()
    unsortedNumbers = [int(n) for n in userInput.split(' ')]

    sortedResult = selectionSort(unsortedNumbers[:])

    print 'The array sorted using selection Sort is:' , sortedResult[0] , 'Execution time' , (sortedResult[2] - sortedResult[1])  

