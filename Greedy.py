"""
Problem: Minimum Remove to Make Valid Parentheses (LeetCode 1249)
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(c)ode)" or "lee(t(co)de)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '(' , ')', or a lowercase English letter.
"""

def min_remove_to_make_valid(s: str) -> str:
    stringlist = list(s)
    stack =[]
    for i in range(len(stringlist)):
        if stringlist[i] == '(':
            stack.append(i)
        elif stringlist[i] == ')' and stack:
            stack.pop()
        elif stringlist[i] == ')' and not stack:
            stringlist[i] = ""
    if stack:
        for i in stack:
            stringlist[i] = ""
    return "".join(stringlist)
"""
Problem: Subarray Sum Equals K (LeetCode 560)
Given an array of integers nums and an integer k, return the total number
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1, 1, 1], k = 2
Output: 2

Example 2:
Input: nums = [1, 2, 3], k = 3
Output: 2

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

from typing import List


"""
Problem: Subarray Sum Equals K (LeetCode 560)
Find total number of continuous subarrays whose sum equals k.
Pattern: Prefix Sum + Hash Map
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
  count = 0
  current_sum = 0
  # Base case: a prefix sum of 0 has occurred once (before elements start)
  prefix_counts = {0: 1}

  for num in nums:
    # 1. Absorb the current number into the running sum
    current_sum += num

    # 2. Check if (current_sum - k) was seen before
    target = current_sum - k
    if target in prefix_counts:
      count += prefix_counts[target]

    # 3. Record the current prefix sum in the frequency map
    prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

  return count
"""
Problem: Longest Substring Without Repeating Characters (LeetCode 3)
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    stringlist = list(s)
    maxval = 0
    left = 0
    mapchar ={}
    if len(stringlist) == 0:
        return maxval
    for i in range(len(stringlist)):
        if mapchar and stringlist[i] in mapchar:
            left = max(left,mapchar[stringlist[i]] + 1)
        mapchar[stringlist[i]] = i
        maxval = max(maxval,i - left + 1)

    return maxval
"""
Problem: Longest Substring Without Repeating Characters (LeetCode 3)
Find the length of the longest substring without repeating characters.

Pattern: Sliding Window with Hash Map (Index Jump)
Time Complexity: O(N) - Single pass through the string
Space Complexity: O(min(N, M)) - Auxiliary space for the character map (M is alphabet size)
"""

def length_of_longest_substring(s: str) -> int:
    max_len = 0
    left = 0
    last_seen = {}

    for right, char in enumerate(s):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
"""
Problem: Gas Station (LeetCode 134)
There are n gas stations along a circular route, where the amount of gas
at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to
travel from the ith station to its next (i + 1)th station. You begin the
journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's
index if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Example 1:
Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2, 3, 4], cost = [3, 4, 3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    curr = 0
    start = 0
    for i in range(len(gas)):
        curr = curr - cost[i] + gas[i]
        if curr < 0:
            start = i+1
            curr = 0
    return start
"""
Problem: Gas Station (LeetCode 134)
Find the starting gas station's index if you can travel around the circuit once.

Pattern: Greedy Reset
Time Complexity: O(N) - Linear pass through gas and cost arrays.
Space Complexity: O(1) - Constant auxiliary space.
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
  # If total gas available across the circle is less than total cost, completion is impossible
  if sum(gas) < sum(cost):
    return -1

  curr_tank = 0
  start_station = 0

  for i in range(len(gas)):
    curr_tank += gas[i] - cost[i]

    # If the tank drops below 0, no station from start_station up to i can be valid
    if curr_tank < 0:
      start_station = i + 1
      curr_tank = 0

  return start_station

"""
Problem: Jump Game II (LeetCode 45)
You are given a 0-indexed array of integers nums of length n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are
generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2, 3, 1, 1, 4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2, 3, 0, 1, 4]
Output: 2

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


def jump(nums: List[int]) -> int:
    if not nums:
        return 0
    j = 0
    farthest = 0
    current_end = 0
    for i in range(len(nums)-1):
        farthest = max(farthest,i + nums[i])
        if i == current_end:
            current_end = farthest
            j += 1
    return j
"""
Problem: Jump Game II (LeetCode 45)
Find the minimum number of jumps to reach the last index.

Pattern: Greedy Range Expansion (Implicit BFS)
Time Complexity: O(N) - Single pass through nums up to index n - 2
Space Complexity: O(1) - Constant auxiliary space
"""

from typing import List


def jump(nums: List[int]) -> int:
  jumps = 0
  current_end = 0
  farthest = 0

  # Only loop up to the second-to-last index
  for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])

    # Exhausted current jump range; commit to next jump
    if i == current_end:
      jumps += 1
      current_end = farthest

  return jumps