import re


def solution(n):
    a = binaryConversion(n)
    b = maximalOnes(a)
    return binaryPlateau(b)


def binaryConversion(n):
    return "{0:b}".format(n)


def maximalOnes(binary_string):
    return re.split('0', binary_string)


def binaryPlateau(ones_list):
    sorted_ones = sorted(ones_list, key=len)
    return len(sorted_ones[-1])
