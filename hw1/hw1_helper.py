import itertools
import math
from hw1 import graph


def left_non_overlap(left, right):
    """Returns the length of the longest suffix of left that is a prefix of right"""
    #
    # YOUR CODE HERE
    non_overlap = left
    if not left or not right:
        return left
    shorter_string_len = len(left) if left < right else len(right)
    for i in range(shorter_string_len):
        if left[-i - 1:] == right[:i + 1]:
            non_overlap = left[:-i-1]

    return non_overlap

def merge_two_strings(left, right):
    left_nonoverlap = left_non_overlap(left, right)
    merged_string = left_nonoverlap + right
    return merged_string

def merged_string_length(left, right):
    return len(merge_two_strings(left,right))

def overlap_length(left,right):
    return len(left) - len(left_non_overlap(left,right))

def merge_ordered_reads(reads):
    """Returns the shortest superstring resulting from merging
    the elements of reads, an ordered list of strings"""
    #
    # YOUR CODE HERE
    superstring = ''
    for read in reads:
        superstring = ''.join(merge_two_strings(superstring, read))
    return superstring


def shortest_superstring(reads):
    """Returns the shortest superstring of reads, a list of strings.
    In the case of multiple shortest superstrings, the lexicographically smallest is returned.
    Assumes that no string in the input is a substring of another input string.
    """
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact = fact * i
#         return fact
#
#         #
# #     permutations = itertools.permutations(reads)
#     shortest_superstring = ''
#     shortest_length = float('+inf')
#     num_permutations = factorial(len(reads))
#     for i,p in enumerate(permutations):
#         print("[]% {}/{}   : {}".format(round(i/num_permutations*1000)/10,i,num_permutations,p))
# #        print(p)
# #        print(shortest_superstring)
#         superstring = merge_ordered_reads(p)
# #        print(superstring)
#         if len(superstring) < shortest_length:
#             shortest_superstring = superstring
#             shortest_length = len(superstring)
#         elif len(superstring) == shortest_length and superstring < shortest_superstring:
#             shortest_superstring = superstring
    return shortest_superstring