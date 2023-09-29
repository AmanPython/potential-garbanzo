## Dynamic Programming

## Introduction
 - [Recursive Solution](#recursive-solution) : Easy to find the solution, usually same function is called many times, overlapping of problems, either timelimit exceeds or stack overflows.
 - [Memoization](#memoization) : This solved the overlapping problems, happend in recursive solution. As per Aditya Verma, their is one problem, matrix multiplications, where stack overflows, all other places, this solves problems efficiently.
 - [Iterative Solution](#iterative-solution) : Here stack overflow won't be problem. This is the most prefered solution, but writing this solution directly is queit hard. 

## Recursive Solution
1. Knapsack Problems
 - Write Recursive Solution ( should not be in backtrack style, should be from n to 0)
 - Question : Subset Sum. From given array, is their a solution, which returns the target sum, from the subsets of array. A subsets is formed by selecting arbitrary values from a set. 
 - Eg: Input: arr = [2,3,7], sum = 5.   Output: True (2+3)
 ```python
 class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        # Recursive Solution
        if sum == 0:
            return True
        elif N == 0 and sum != 0:
            return False
        if sum - arr[N-1] >= 0:
            return self.isSubsetSum(N-1,arr,sum-arr[N-1]) or self.isSubsetSum(N-1,arr,sum)
        else:
            return self.isSubsetSum(N-1,arr,sum)
 ```

 ## Memoization
 - Convert Recursive Solution to Memoization
 ```python
 class Solution:
    def helperFun(self,N,arr,sum,dp):
        if sum == 0:
            return True
        elif N == 0 and sum != 0:
            return False
        if dp[sum][N] != -1:
            return dp[sum][N]
        if sum - arr[N-1] >= 0:
            dp[sum][N] = self.helperFun(N-1,arr,sum-arr[N-1],dp) or self.helperFun(N-1,arr,sum,dp)
            return dp[sum][N]
        else:
            dp[sum][N] = self.helperFun(N-1,arr,sum,dp)
            return dp[sum][N]
    def isSubsetSum (self, N, arr, sum):
        # code here 
        ## Initialize DP
        dp = [[-1]*(N+1) for _ in range(sum+1)]
        ## Initialize the initial value
        for i in range(sum+1):
            dp[i][0] = True
        self.helperFun(N,arr,sum,dp)
        return dp[sum][N]
 ```
 - Steps:
    - Step 1 : In recursive functions, the changing variables are N and sum, so form 
    a matrix and store the values, usually dp[array index][Knapsack beg weight] as dp[N][sum]
    - Step 2 : Use the base condition to initialize the array, think and put their values. 
    ```python
    ## Initialize DP
    dp = [[-1]*(N+1) for _ in range(sum+1)]
    ```
    - Step 3 : Use as Cache and create seprate helper function, or can use dp = 0, and if condition to initialze for the first time.
    ```python
    if dp[sum][N] != -1:
    return dp[sum][N]
    ```
    - Step 4 : Recursion call function :

    ```python
    if sum - arr[N-1] >= 0:
        dp[sum][N] = self.helperFun(N-1,arr,sum-arr[N-1],dp) or self.helperFun(N-1,arr,sum,dp)
        return dp[sum][N]
    else:
        dp[sum][N] = self.helperFun(N-1,arr,sum,dp)
        return dp[sum][N]
    ```


## Iterative Solution
 - Convert all Recursion to iterative Solution
 ```python
 class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
         dp = [[0]*(sum+1) for _ in range(N+1)]

        ## initialize dp
        for i in range(N+1):
            dp[i][0] = 1

        for i in range(1,N+1):
            for j in range(1,sum+1):
                if j - arr[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][sum]
 ```
 - Steps:
    - Step 1 : Convert Recursion Postion to dp matrix
    ```python
        ## Initialize the initial value
        for i in range(sum+1):
            dp[i][0] = True
    ```
    | sum->| 0 | 1 | 2 | 3 | 4 | 5 | 
    |----|----|----|----|----|---| --|
    |(N->0) | T  | F  | F | F | F | F |
    | 2 (1)| T | -1 | -1 |-1 |-1 |-1 |
    | 3 (2)| T | -1 |-1 |-1 |-1 |-1 |
    | 7 (3)| T | -1 |-1 |-1 |-1 |-1 |
    #### Or initialize where 1 -> True, 0 -> False, -1 -> Not Calculated
    - At the end, return 1 == dp[N][sum]

    | sum->| 0 | 1 | 2 | 3 | 4 | 5 | 
    |----|----|----|----|----|---| --|
    |(N->0) | 1  | 0  | 0 | 0 | 0 | 0 |
    | 2 (1)| 1 | -1 | -1 |-1 |-1 |-1 |
    | 3 (2)| 1 | -1 |-1 |-1 |-1 |-1 |
    | 7 (3)| 1 | -1 |-1 |-1 |-1 |-1 |

    - Step 2 : Remove all the recursion Logic and solve it iteratively.
    ## From code
    ```python
    if sum - arr[N-1] >= 0:
        dp[sum][N] = self.helperFun(N-1,arr,sum-arr[N-1],dp) or self.helperFun(N-1,arr,sum,dp)
        return dp[sum][N]
    else:
        dp[sum][N] = self.helperFun(N-1,arr,sum,dp)
        return dp[sum][N]
    ```
    ## To code ( N changes to i and Sum changes to j)
    ```python
    for i in range(1,N+1):
        for j in range(1,sum+1):
            if j - arr[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j-arr[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    ```
    - If True False are used, use the or condition.
    - Their could be other possible itertive solutions, like this problem has one dimensional array solution, but this is far most easiest way to solve.
