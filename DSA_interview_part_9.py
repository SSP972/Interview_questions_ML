'''
<aside>
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**
Input: n = 1 

Output: true

**Example 2:**
Input: n = 16 

Output: true

**Example 3:**
Input: n = 3 

Output: false

</aside>

<aside>
💡 **Question 2**

Given a number n, find the sum of the first natural numbers.

**Example 1:**

Input: n = 3 

Output: 6

**Example 2:**

Input  : 5 

Output : 15

</aside>

<aside>
💡 **Question 3**

****Given a positive integer, N. Find the factorial of N. 

**Example 1:**

Input: N = 5 

Output: 120

**Example 2:**

Input: N = 4

Output: 24

</aside>

<aside>
💡 **Question 4**

Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

**Example 1 :** 

Input: N = 5, P = 2

Output: 25

**Example 2 :**
Input: N = 2, P = 5

Output: 32

</aside>

<aside>
💡 **Question 5**

Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

**Example 1:**

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: 8

**Example 2:**

Input: arr = {1, 4, 45, 6, 10, -8};
Output: 45

</aside>

<aside>
💡 **Question 6**

Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.

**Example 1:**

Input : a = 2 d = 1 N = 5
Output : 6
The 5th term of the series is : 6

**Example 2:**

Input : a = 5 d = 2 N = 10
Output : 23
The 10th term of the series is : 23

</aside>

<aside>
💡 **Question 7**

Given a string S, the task is to write a program to print all permutations of a given string.

**Example 1:**

***Input:***

*S = “ABC”*

***Output:***

*“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

**Example 2:**

***Input:***

*S = “XY”*

***Output:***

*“XY”, “YX”*

</aside>

<aside>
💡 **Question 8**

Given an array, find a product of all array elements.

**Example 1:**

Input  : arr[] = {1, 2, 3, 4, 5}
Output : 120
**Example 2:**

Input  : arr[] = {1, 6, 3}
Output : 18

</aside>


'''
# 💡 Question 1

  
def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
# Time complexity: O(1)
# Space complexity: O(1)

# 💡 Question 2

  
def sumOfFirstN(n):
    return (n * (n + 1)) // 2
# Time complexity: O(1)
# Space complexity: O(1)

# 💡 Question 3

  
def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N - 1)
# Time complexity: O(N)
# Space complexity: O(N) (due to recursion)

# 💡 Question 4

  
def power(N, P):
    return N ** P
# Time complexity: O(P)
# Space complexity: O(1)

# 💡 Question 5

  
def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], findMax(arr[1:]))
# Time complexity: O(N)
# Space complexity: O(N) (due to recursion)

# 💡 Question 6

  
def nthTerm(a, d, N):
    return a + (N - 1) * d
# Time complexity: O(1)
# Space complexity: O(1)

# 💡 Question 7

  
def permutations(S):
    if len(S) == 1:
        return [S]
    
    result = []
    for i in range(len(S)):
        char = S[i]
        remaining = S[:i] + S[i+1:]
        for p in permutations(remaining):
            result.append(char + p)
    
    return result
# Time complexity: O(n!)
# Space complexity: O(n!) (due to the number of permutations)

# 💡 Question 8

  
def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product
# Time complexity: O(N)
# Space complexity: O(1)