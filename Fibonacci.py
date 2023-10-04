def fibonacci(n):
    """
    Tagastab n-nda Fibonacci numbri.
    n (int): Fibonacci järjekorranumber, mida soovime leida. Peab olema mittenegatiivne täisarv.
    Tagastab:
    int: n-nes Fibonacci numbri.
    """
    # Kui n on 0 või 1, siis tagastame vastavalt 0 või 1, kuna Fibonacci jada algab nendest arvudest.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# näiteks:
n = 10
fibonacci_number = fibonacci(n)
print(f"{n}-nes Fibonacci number on {fibonacci_number}")