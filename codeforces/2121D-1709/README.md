# 2121D-1709

**Problem:** [2121D-1709](https://codeforces.com/contest/2121/problem/D)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

You are given two arrays of integers a_1, a_2, …, a_n and b_1, b_2, …, b_n. It is guaranteed that each integer from 1 to 2 ⋅ n appears in exactly one of the arrays.

You need to perform a certain number of operations (possibly zero) so that both of the following conditions are satisfied:

-  For each 1 ≤q i  \lt  n, it holds that a_i  \lt  a_{i + 1} and b_i  \lt  b_{i + 1}. 
-  For each 1 ≤q i ≤q n, it holds that a_i  \lt  b_i. 
During each operation, you can perform exactly one of the following three actions:

-  Choose an index 1 ≤q i  \lt  n and swap the values a_i and a_{i + 1}. 
-  Choose an index 1 ≤q i  \lt  n and swap the values b_i and b_{i + 1}.
-  Choose an index 1 ≤q i ≤q n and swap the values a_i and b_i.You do not need to minimize the number of operations, but the total number must not exceed 1709. Find any sequence of operations that satisfies both conditions.


**Input**

Each test consists of multiple test cases. The first line contains a single integer t (1 ≤q t ≤q 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤q n ≤q 40) — the length of the arrays a and b.

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤q a_i ≤q 2 ⋅ n).

The third line of each test case contains n integers b_1, b_2, …, b_n (1 ≤q b_i ≤q 2 ⋅ n).

It is guaranteed that each integer from 1 to 2 ⋅ n appears either in array a or in array b.


**Output**

For each test case, output the sequence of operations. 

In the first line for each test case, output the number of operations k. Note that 0 ≤q k ≤q 1709. 

In the following k lines for each test case, output the operations themselves:

-  If you want to swap the values a_i and a_{i + 1}, output two integers 1 and i. Note that 1 ≤q i  \lt  n.
-  If you want to swap the values b_i and b_{i + 1}, output two integers 2 and i. Note that 1 ≤q i  \lt  n.
-  If you want to swap the values a_i and b_i, output two integers 3 and i. Note that 1 ≤q i ≤q n.
It can be shown that under the given constraints, a solution always exists.


**Example**

**Input**

```
6
1
1
2
1
2
1
2
1 3
4 2
2
1 4
3 2
3
6 5 4
3 2 1
3
5 3 4
2 6 1
```

**Output**

```
0
1
3 1
1
2 1
1
3 2
9
3 1
3 2
3 3
1 1
2 1
2 2
1 2
1 1
2 1
6
2 2
1 1
1 2
2 1
3 1
3 2
```


**Note**

In the first test case, a_1  \lt  b_1, so no operations need to be applied. 

In the second test case, a_1  \gt  b_1. After applying the operation, these values will be swapped. 

In the third test case, after applying the operation, a = [1, 3] and b = [2, 4]. 

In the fourth test case, after applying the operation, a = [1, 2] and b = [3, 4].
