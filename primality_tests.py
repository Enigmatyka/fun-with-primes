# different methods of checking whether a given integer is a prime number

from math import sqrt

# the most obvious straightforward way to deal with this O(sqrt n)
def isPrime_naive_first(integer):
    if integer <=1:
        return False

    for i in range(2, int(sqrt(integer)) + 1):
        if (integer % integer == 0):
            return False
    return True

# grabbed from geeksforgeeks.org
# all primes greater than 3 are of the form 6k ± 1

def isPrimeBetter(integer):
    if integer <=1:
        return False
    
    if integer in (2, 3):
        return True
    elif integer <= 1 or integer % 2 == 0 or integer % 3 == 0:
        return False

    for i in range(5, int(sqrt(integer)) + 1, 6):
        if integer % i == 0 or integer % (i + 2) == 0:
            return False

    return True