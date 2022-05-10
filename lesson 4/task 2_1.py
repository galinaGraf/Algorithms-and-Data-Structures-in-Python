#Написать два алгоритма нахождения i-го по счёту простого числа.
n = 10000

def sieve_eratosfen_(index):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i

    prime = [i for i in sieve if i != 0]
    return (prime[index])

print(sieve_eratosfen_1(0))