#!/usr/bin/env bash
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n == 1:
        return [n]
    if n % 2 == 0:
        return [2, n // 2]

    x = 2
    y = 2
    d = 1

    f = lambda x: (x ** 2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    
    if d == n:
        return "Failed to factorize, try another method"
    
    return [d, n // d]

# Your number to factorize
n = 2497885147362973

factors = pollards_rho(n)
print(f"{n}={factors[0]}*{factors[1]}")

