# TO-DO: Complete the selection_sort() function below 
testArr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap is True:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp1 = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp1
                swap = True


    return arr


print(bubble_sort(testArr))
print(selection_sort(testArr))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr