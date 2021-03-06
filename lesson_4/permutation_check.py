"""Main script for permutation_check.py"""

# A non-empty array A consisting of N integers is given.
#
# A permutation is a sequence containing each element from 1 to N once, and only once.
#
# For example, array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
#
# The goal is to check whether array A is a permutation.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
# More explicitly, check if a given a array strictly .
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.
#
# Given array A such that:
#
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


def solution(A):
    """Returns true if a permutation sequence."""
    seen = [False] * len(A)

    for value in A:
        if 0 <= value > len(A):
            return 0
        if seen[value - 1]:
            return 0
        seen[value - 1] = True

    return 1


if __name__ == "__main__":
    test_array = [0]*100000
    count = -10
    for i in range(0, 100000):
        test_array[i] = count
        count += 1
