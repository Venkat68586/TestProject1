def counting_sort(arr):
    max_value = max(arr)
    
    count_array = [0] * (max_value + 1)
    
    for num in arr:
        count_array[num] += 1
    
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i] * count_array[i])
    
    return sorted_array

input_list = [4, 2, 2, 8, 3, 3, 1]
sorted_list = counting_sort(input_list)
print("Sorted array:", sorted_list)
