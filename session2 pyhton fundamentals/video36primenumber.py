count=0
n=(int)(input("Enter the range="))
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    
    if is_prime:
        print(i)
        
        
        
        
# sieve method
n = int(input("Enter n: "))

# Assume all numbers are prime
prime = [True] * (n + 1)

prime[0] = False
prime[1] = False

p = 2

while p * p <= n:

    if prime[p]:

        # Mark multiples of p as False
        for i in range(p * p, n + 1, p):
            prime[i] = False

    p += 1

# Print primes
for i in range(2, n + 1):
    if prime[i]:
        print(i)