def largest_prime_factor(n):
    largest_factor = None
    
    while n % 2 == 0:
        largest_factor = 2
        n = n/2

    for i in range(3, int(n**0.5) +1,2):
        while n % i == 0:
            largest_factor = i
            n = n/i

    return largest_factor

x = int(input('Int: '))
print(largest_prime_factor(x))
