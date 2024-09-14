# O(n^2) time
# Requires: array

def selection_sort(array):
    sorted_array = []

    for i in range(1, len(array)):
        smallest = find_smallest(array)
        sorted_array.append(array.pop(smallest))

    return sorted_array



def find_smallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index

res = selection_sort([5, 3, 6, 2, 10])
print(res)