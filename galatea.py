import functools
import time


# timing function using decorators
def timer(func):
    # Print the runtime of the decorated function
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} seconds')
        return value

    return wrapper_timer


# Decorating is_prime with timer

@timer
def is_prime(input):
    n = int(input)
    # Creating a list of 1 where 1 - is prime, 0 - not prime
    primes = [1] * (n + 1)
    # We know that 0 and 1 are not prime
    primes[0], primes[1] = 0, 0
    # We start checking from 2
    i = 2

    # We want to check whether numbers from 2 to n are prime
    while i * i <= (n + 1):
        # If we already checked this number then we skip checking it again
        if primes[i] == 0:
            i += 1
            continue
        # We start checking the multiplies of i
        j = i * 2
        while j < (n + 1):
            primes[j] = 0
            j += i
        i += 1

    if primes[n] == 1:
        return True
    else:
        return False

# Running the decorated function with an example input
is_prime(439868)

# pytest simple tests
class TestClass:
    def test_is_primes(self):
        assert is_prime(71) is True
        assert is_prime(439867) is True
        assert is_prime(5876389) is True
        assert is_prime(439868) is False
        assert is_prime(102390212) is False
