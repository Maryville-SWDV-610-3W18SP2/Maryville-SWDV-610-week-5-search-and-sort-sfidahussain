#Consider the following list of integers: [1,2,3,4,5,6,7,8,9,10].
#Show how this list is sorted by the following algorithms:
#bubble sort
#selection sort
#insertion sort

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        print(alist)
        
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        print(alist)

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
        print(alist)

def main():
    alist = [10, 5, 3, 4, 1, 8, 9, 7, 2, 6]
    print('Bubble Sort')
    bubbleSort(alist)
    alist = [10, 5, 3, 4, 1, 8, 9, 7, 2, 6]
    print('Selection Sort')
    selectionSort(alist)
    alist = [10, 5, 3, 4, 1, 8, 9, 7, 2, 6]
    print('Insertion Sort')
    insertionSort(alist)

main()


