# Complete this function

# T.C = O(n*n)

def trappingWater(arr, n):
    # Your code her
    total_water = 0
    for i in range(1, n):
        leftmax = max(arr[0:i+1])
        rightmax = max(arr[i:])
        total_water = total_water + min(leftmax, rightmax) - arr[i]
        print(leftmax,rightmax,total_water)
    return total_water

def trappingWater2(arr, n):
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0] * n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0] * n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # Fill right array
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water
# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        print(trappingWater(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends