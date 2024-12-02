def largest_square_number(n):
    m = 0
    while (m + 1) ** 2 <= n:
        m += 1
    q = m ** 2
    return q

n = int(input("Enter a natural number n: "))
result = largest_square_number(n)
print(f"The largest square number less than or equal to {n} is {result}.")
