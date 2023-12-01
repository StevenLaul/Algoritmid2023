def trivial_hashing(arr):
    max_val = max(arr)
    index_map = [-1] * (max_val + 1)

    for i in range(len(arr)):
        index = arr[i]
        if index_map[index] == -1:
            index_map[index] = i
        else:
            print(f"Collision at index {index}, current value: {arr[index_map[index]]}, new value: {arr[i]}")

    return index_map

# Näide:
input_array = [4, 2, 8, 3, 6, 1, 7, 9, 5]
result = trivial_hashing(input_array)
print("Index Mapping:", result)