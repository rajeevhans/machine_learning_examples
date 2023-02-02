import numpy as np

unsorted_array = [107,3,5,1,8,12,55]

print("Unsorted array", unsorted_array)


def bubbleSort(input_array):
    arraySize = len(input_array)

    for i in range(arraySize):
        for j in range(arraySize - 1):
            if input_array[i] < input_array[j]:
                temp = input_array [i]
                input_array [i] = input_array [j]
                input_array [j] = temp
    return input_array
                
sorted_array = bubbleSort (unsorted_array)

print("Sorted array", unsorted_array)
