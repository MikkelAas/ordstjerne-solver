# takes in an array of characters and makes them all lower case
from numpy import char


def lowerArray(array):
    for i in range(len(array)):
        array[i] = array[i].lower()
    return array
