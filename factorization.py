#!/usr/bin/env bash
import math

def factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        num = int(num)
        factors = factorize(num)
        # Assuming two factors for each number
        if len(factors) >= 2:
            print(f"{num}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        file_path = sys.argv[1]
        factorize_file(file_path)
