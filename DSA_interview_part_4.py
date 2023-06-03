#💡 Question 1

#To find the integers that appear in all three sorted arrays, we can use three pointers to iterate 
#through the arrays. We increment the pointers when the current elements are smaller than the
#maximum element among the three. If all three elements are the same, we add it to the result 
#list. Otherwise, we increment the pointer of the array with the smallest element.    

   
   
def arraysIntersection(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        max_val = max(arr1[i], arr2[j], arr3[k])
        
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            if arr1[i] < max_val:
                i += 1
            if arr2[j] < max_val:
                j += 1
            if arr3[k] < max_val:
                k += 1
    
    return result
#Time complexity: O(n)
#Space complexity: O(1)

#💡 Question 2

#To find the distinct integers present in nums1 and not in nums2, and vice versa, we can use 
#sets to store the unique elements and then find the set differences.    

   
   
def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)
    
    return [list(diff1), list(diff2)]
#Time complexity: O(n)
#Space complexity: O(n)

#💡 Question 3

#To find the transpose of a matrix, we can iterate through each element in the matrix and swap #the row and column indices.    

   
   
def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    transposed = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    
    return transposed
#Time complexity: O(m * n)
#Space complexity: O(m * n)

#💡 Question 4

#To maximize the sum of minimum pairs, we need to pair the smallest elements together. 
# Sorting the array and pairing consecutive elements will ensure that the minimum elements are paired together.    

   
   
def arrayPairSum(nums):
    nums.sort()
    n = len(nums)
    pair_sum = 0
    
    for i in range(0, n, 2):
        pair_sum += nums[i]
    
    return pair_sum
#Time complexity: O(n log n) (due to sorting)
#Space complexity: O(1)

#💡 Question 5

#The number of complete rows in the staircase is equal to the largest number k such that k * (k + 1) / 2 is less than or equal to n. We can find k by solving the quadratic equation (k^2 + k) / 2 = n.    

   
   
def arrangeCoins(n):
    k = int((2 * n) ** 0.5) - 1
    while (k + 1) * (k + 2) // 2 <= n:
        k += 1
    return k
#Time complexity: O(sqrt(n))
#Space complexity: O(1)

#💡 Question 6

#To square each number in the array and sort it in non-decreasing order, we can square each #element and then sort the resulting array.    

   
   
def sortedSquares(nums):
    return sorted(num * num for num in nums)
#Time complexity: O(n log n) (due to sorting)
#Space complexity: O(n)

#💡 Question 7

#To count the number of maximum integers after performing the given operations, we need to 
#find the smallest dimensions of the matrix that will be incremented. The product of these #dimensions will give us the count of maximum integers.    

   
   
def maxCount(m, n, ops):
    min_row = m
    min_col = n
    
    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])
    
    return min_row * min_col
#Time complexity: O(k), where k is the length of the ops list
#Space complexity: O(1)

#💡 Question 8

#To reorder the elements in the given manner, we can create a new list and alternate between 
#taking elements from the first half and second half of the input array.    

   
   
def shuffle(nums, n):
    result = []
    
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    
    return result
#Time complexity: O(n)
#Space complexity: O(n)

