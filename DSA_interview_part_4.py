'''
<aside>
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

</aside>

<aside>
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

</aside>

<aside>
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**
https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa54805f4-c9b5-491c-a900-8e8a94062c79%2Fiamge_v3.png?id=a588d9bb-578d-4c0f-b2fe-813f5225886b&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=1020&userId=&cache=v2
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]



</aside>

<aside>
💡 **Question 4**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.

**Example 1:**
https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b%2Fv2.jpg?id=011c94c5-b725-4954-8821-3900e6c08ab4&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=510&userId=&cache=v2
Input: nums = [1,4,3,2]

Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3

2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3

3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

So the maximum possible sum is 4.

</aside>

<aside>
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

[]()

![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

</aside>

<aside>
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

</aside>

<aside>
💡 **Question 7**
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

**Example 1:**

https://pwskills.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4d0890d0-7bc7-4f59-be8e-352d9f3c1c52%2Fq4.jpg?id=90aeb3cb-54bb-4240-9291-1fce694e3fe9&table=block&spaceId=6fae2e0f-dedc-48e9-bc59-af2654c78209&width=1020&userId=&cache=v2

**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

**Output:** 4

**Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

</aside>

<aside>
💡 **Question 8**

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3

**Output:** [2,3,5,4,1,7]

**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

</aside>
'''



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

