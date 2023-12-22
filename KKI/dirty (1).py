"""Module has a function that prints the name of my site"""
import random
import numpy as np

DEFAULT_ACCURACY = 3


def sum_two_values(first, second):
    """Function printing python version."""
    return first + second


def div(x, y, accuracy):
    """Function printing python version."""
    return round(x/y,  accuracy)



def get_rand():
    """Function printing python version."""
    return random.randint(1, 10)

def rand_array():
    """Function printing python version."""
    a = [get_rand(), get_rand(), get_rand()]
    return np.array(a)

def main():
    """Function printing python version."""


main()
