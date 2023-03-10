import logging
import functools
from math import sqrt
from time import time, perf_counter
from dataclasses import dataclass
from abc import ABC, abstractmethod


# excluding cross-cutting concers
def is_prime(number: int) -> bool:

    if number < 2:
        return False
    for element in range(2, int(sqrt(number))+1):
        if (number % element) == 0:
            return False
    return True
    
# decorator function  
def benchmark(func: callable) -> callable:
    # the wrapper function
    def wrapper(*args, **kwargs) -> any:
        start = perf_counter()
        val = func(*args, **kwargs)
        end = perf_counter()
        run_time = end - start
        logging.info(f'Prime conter took {run_time:.2f} seconds')
        return val
    # returning the wrapper funtion
    return wrapper

# decorating our [STAR] function
@benchmark
def count_primes(upper_bound: int) -> int:
    count = len([number for number in range(upper_bound) if is_prime(number)])
    return count

# the runner function
def main() -> None:
    logging.basicConfig(level=logging.INFO)
    val = count_primes(100000)
    logging.info(f'Number of primes: {val}')

# print(count_primes(100))

if __name__ == '__main__':
    main()