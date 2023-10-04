def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 'target' leiti, tagastame indeksi
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "Täisarvu ei leitud."

# Näiteks:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(sorted_list, target)

if isinstance(result, int):
    print(f"{target} leiti indeksil
    {result}.")
else:
    print(result)