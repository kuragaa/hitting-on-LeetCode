# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

# Algorithm:
# 1) Find the number of zeros which would be duplicated.
#    We do need to make sure we are not counting the zeros which would be trimmed off. Since, the discarded zeros won't be part of the final array.
#    Special case: the edge of the array is 0 and we have no space to duplicate it: [8,4,5,0,0,0,0,7] -> [8,4,5,0,0,0,0,0]
#    |
#    To handle this we should not count zero element that has i = n - 1 - z (index of the edge) and copy it to the edge of the actual array,
#    then we should decrease len(arr) - 1 so we won't touch the last (in final array) element while duplicating zeros
# 2) Find the index that will be the edge of the final array (len(arr) - zeros)
# 3) Iterate the array from the end and copy a non-zero element once and zero element twice (except zero that is the edge of he final array)

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        n = len(arr)
        zeros = 0
        count = 0

        for i in range(n):
          if count >= n:  # not count elements which would be trimmed off
            break
          if arr[i] == 0:
            if i == n - 1 - zeros:  # if zero element has edge index of the final array
              arr[n-1] = 0  # we copy it to the edge index of actual array
              n -= 1  # decrease len of array, so we won't duplicate that one zero
              break  # stop counting - we reached the limit of space
            count += 1
            zeros += 1
          count +=1

        index = n - zeros - 1

        for i in range(index, -1, -1):
          if arr[i] == 0:
            arr[i+zeros] = 0
            zeros -= 1
            arr[i+zeros] = 0
          else:
            arr[i+zeros] = arr[i]

