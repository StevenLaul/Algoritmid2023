def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Kui elementi ei leia siis tagastab indeksi
    return -1  # Elementi ei leitud, tagastab -1