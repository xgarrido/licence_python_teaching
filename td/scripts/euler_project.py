"""
Module for Euler projects

This file holds several solution of Euler project
"""

def euler001(n=None):
    """Solution for Euler project n°1

    Find the sum of all the multiples of 3 or 5 below n.

    """
    if n == None:
        n = int(input("Give the n value : "))
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])

def euler002(n=None):
    """Solution for Euler project n°2

    By considering the terms in the Fibonacci sequence whose values do not
    exceed a given value, find the sum of the even-valued terms.

    """
    if n == None:
        n = int(input("Give the n value : "))
    f, g, somme = 1, 1, 0
    while f < n:
        if f % 2 == 0:
            somme += f
        f, g = g, f+g
    return somme

def euler006(n=None):
    """Solution of Euler project n°6

    Find the difference between the sum of the squares of the first n natural
    numbers and the square of the sum.

    """
    if n == None:
        n = int(input("Give the n value : "))
    r = range(1, n+1)
    return sum(r)**2 - sum([x**2 for x in r])

def euler016(n=None):
    """Solution for Euler project n°16

    What is the sum of the digits of the number 2**n?

    """
    if n == None:
        n = int(input("Give the n value : "))
    somme = 0
    for i in str(2**n):
        somme += int(i)
    return somme

def euler025(n=None):
    """Solution for Euler project n°25

    What is the index of the first term in the Fibonacci sequence to contain n digits?

    """
    if n == None:
        n = int(input("Give the n value : "))
    f, g, i = 1, 1, 0
    while f < 10**n:
        f, g, i = g, f+g, i+1
    return i

projects = {1 : euler001, 2 : euler002, 6 : euler006, 16 : euler016, 25 : euler025}

if __name__ == "__main__":
    i = 0
    while True:
        i = int(input("Project number ? "))
        if i not in projects.keys():
            print("Project n°{} not solved yet".format(i))
            continue
        print(projects[i]())
        break
