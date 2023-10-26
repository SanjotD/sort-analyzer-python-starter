# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])

# Menu
loop = True
while loop:
    userSelect = menuSelect()

    if userSelect == "1":
        print("Bubble Sort")
    elif userSelect == "2":
        print("Selection Sort")
    elif userSelect == "3":
        print("Insertion Sort")
    elif userSelect == "4":
        print("Bye")
        loop = False

# Sort Functions
def bubbleSort(anArray):
    for n in range(len(anArray)-1, 0, -1):
        for i in range(n):
            if anArray[i] > anArray[i+1]:
                anArray[i], anArray[i+1] = anArray[i+1], anArray[i]
                
def selectionSort(anArray):
    for n in range(0, len(anArray)-1):
        minPos = n
        for i in range(n+1, len(anArray)):
            if anArray[i] < anArray[minPos]:
                minPos = i


        anArray[n], anArray[minPos] = anArray[minPos], anArray[n]

def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertVal = anArray[i]
        insertPos = i


        while insertPos > 0 and anArray[insertPos - 1] > insertVal:
            anArray[insertPos] = anArray[insertPos - 1]
            insertPos = insertPos - 1


        anArray[insertPos] = insertVal

# Menu Functions
def menuSelect():
    print("\n Sort Analyzer")
    print("1. Bubble")
    print("2. Selection")
    print("3. Insert")
    print("4. Exit")
    return input ("\nEnter Opt (#):")

def bubble_sort(anArray):
    

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
