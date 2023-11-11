def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Vahetame kohad
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

        # Prindi tulemus
        print(f"Samm {i + 1}: {arr}")

# Algse loendi loomine
arr = [64, 34, 25, 12, 22, 11, 90]

# Alusta Bubble Sorti
print("Algne loend:", arr)
bubble_sort(arr)