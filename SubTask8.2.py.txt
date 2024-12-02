def compute_count(): 

    n = 0   

    s = 0   

    m = float('inf')  

    a = 0   

 

    while True: 

        x = int(input("Enter a number (or -1 to stop): ")) 

        if x == -1: 

            break 

        n += 1 

        s += x 

        if x < m: 

            m = x 

    if n == 0: 

        m = -1 

        a = -1 

    else: 

        a = s / n 

    print(f"Count (n): {n}") 

    print(f"Sum (s): {s}") 

    print(f"Minimum (m): {m}") 

    print(f"Mean (a): {a}") 

compute_count() 
