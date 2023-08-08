def checkPrime(num):
    # Function to check if a number is prime or not
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 
    return num

def twinPrime():
    # Function to generate a list of twin primes less than 1000
    twin_primes = []
    for num in range(3, 1000, 2):  # Considering only odd numbers
        if checkPrime(num) and checkPrime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

twin_primes_list = twinPrime()
print("Twin primes less than 1000:")
for twin_prime in twin_primes_list:
    print(f"{twin_prime[0]} and {twin_prime[1]}")
