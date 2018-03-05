
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# Riiight we need 1 for the unique case between 2 and 3.
freqObject = {1: 0}
freqs = []
freqsOfFreqs = []

primes = []
differences = [];


def isPrime(n):
    # Range goes from bottom to one less than top:
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


# Now, how many of are each distance (e.g. 6) apart from each other? For 2 up to 72.
for i in range(2, 74, 2):
    # print(i)
    freqObject[i] = 0
    freqs.append(i)

print(freqObject)

# There are 9600 primes in range up to 100,000:
for i in range(2, 100000):
    if isPrime(i):
        primes.append(i)

for index, p in enumerate(primes):
    if (index < len(primes) - 1):
        # print(p)
        diff = primes[index + 1] - p
        differences.append(diff)

        freqObject[diff] += 1

# print(differences)
print(len(primes), len(differences))

# Account for extra prime number without a difference to higher prime:
primes = primes[:-1]

# It's nice you can use i every time in python:
for i in range(2, 74, 2):
    freqsOfFreqs.append(freqObject[i])

# plt.scatter(primes, differences, s=0.9)
plt.scatter(freqs, freqsOfFreqs)
plt.xlabel('Difference Values')
plt.ylabel('Frequencies of Differences')

plt.show()
