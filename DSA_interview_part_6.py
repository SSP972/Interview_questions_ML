'''
<aside>
💡 **Question 1**

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

**Input:** s = "IDID"

**Output:**

[0,4,1,3,2]

</aside>

<aside>
💡 **Question 2**

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

You must write a solution in O(log(m * n)) time complexity.

**Example 1:**

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output:** true

</aside>

<aside>
💡 **Question 3**

Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


**Example 1:**

**Input:** arr = [2,1]

**Output:**

false

</aside>

<aside>
💡 **Question 4**

Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

**Example 1:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

</aside>

<aside>
💡 **Question 5**

The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

**Example 1:**

**Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

**Output:** 40

**Explanation:**

We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

</aside>

<aside>
💡 **Question 6**

An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

**Example 1:**

**Input:** changed = [1,3,4,2,6,8]

**Output:** [1,3,4]

**Explanation:** One possible original array could be [1,3,4]:

- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.

Other original arrays could be [4,3,1] or [3,1,4].

</aside>

<aside>
💡 **Question 7**

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

**Example 1:**


**Input:** n = 3

**Output:** [[1,2,3],[8,9,4],[7,6,5]]

</aside>

<aside>
💡 **Question 8**

Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

**Example 1:**



**Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

**Output:**

[[7,0,0],[-7,0,3]]

</aside>
'''


# 💡 Question 1: Reconstruct Permutation

 
def reconstructPermutation(s):
    n = len(s)
    perm = []
    low, high = 0, n
    
    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    
    perm.append(low)
    return perm
# Time complexity: O(n)
# Space complexity: O(1)

# 💡 Question 2: Search in a 2D Matrix

 
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // n][mid % n]
        
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
# Time complexity: O(log(m * n))
# Space complexity: O(1)

# 💡 Question 3: Valid Mountain Array

 
def validMountainArray(arr):
    n = len(arr)
    i = 0
    
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        return False
    
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1
    
    return i == n - 1
# Time complexity: O(n)
# Space complexity: O(1)

# 💡 Question 4: Contiguous Array

 
def findMaxLength(nums):
    count = 0
    max_length = 0
    count_map = {0: -1}
    
    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1
        
        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i
    
    return max_length
# Time complexity: O(n)
# Space complexity: O(n)

# 💡 Question 5: Minimum Product Sum

 
def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    
    return sum(nums1[i] * nums2[i] for i in range(len(nums1)))
# Time complexity: O(n log n)
# Space complexity: O(1)

# 💡 Question 6: Reverse to Make Equal

 
def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []
    
    counts = {}
    original = []
    
    for num in changed:
        counts[num] = counts.get(num, 0) + 1
    
    changed.sort()
    
    for num in changed:
        if counts[num] == 0:
            continue
        
        counts[num] -= 1
        half_num = num // 2
        
        if counts.get(half_num, 0) == 0:
            return []
        
        counts[half_num] -= 1
        original.append(half_num)
    
    return original
# Time complexity: O(n log n)
# Space complexity: O(n)

# 💡 Question 7: Spiral Matrix II

 
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    num = 1
    
    while row_start <= row_end and col_start <= col_end:
        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1
        
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1
        
        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                matrix[row_end][j] = num
                num += 1
            row_end -= 1
        
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1
    
    return matrix
# Time complexity: O(n^2)
# Space complexity: O(n^2)

# 💡 Question 8: Sparse Matrix Multiplication

 
def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for x in range(k):
                result[i][j] += mat1[i][x] * mat2[x][j]
    
    return result
# Time complexity: O(m * k * n)
# Space complexity: O(m * n)