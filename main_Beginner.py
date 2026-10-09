from inspect import stack


def main():
    # Two Sum
    print("Hello World")


from collections import Counter


# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target. You may assume that each input would have exactly one solution, and you
# may not use the same element twice. You can return the answer in any order.
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []


# 242. Valid Anagram (Frequency Table Approach)
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1

    return True


# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
def contains_duplicate(nums: list[int]) -> bool:
    return any(count >= 2 for count in Counter(nums).values())
def contains_duplicate(nums: list[int]) -> bool:
    result = False
    map = set()
    for num in nums:
        if num in map:
            return True
        else:
            map.add(num)


# 217. Contains Duplicate (Set Length Approach)
# Given an integer array nums, return true if any value appears at least twice in the array.
def contains_duplicate(nums: list[int]) -> bool:
    # set drops duplicates unlike dictionary
    return len(nums) != len(set(nums))


# 217. Contains Duplicate (Early Exit with HashSet)
# Given an integer array nums, return true if any value appears at least twice in the array.
def contains_duplicate(nums: list[int]) -> bool:
    duplicates = set()
    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False


# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock. Return the maximum profit you can achieve from
# this transaction. If you cannot achieve any profit, return 0.
def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Given a string s, return true if it is a palindrome, or false otherwise.
def is_palindrome(s: str) -> bool:
    n = ""
    for ch in s:
        if ch.isalnum():
            n += ch.lower()
    return n == n[::-1]


# 643. Maximum Average Subarray I (Brute Force / Slice Sum - O(n*k))
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value
# and return this value.
# O(n*k) which is incorrect need to get O(n)
def find_max_average(nums: list[int], k: int) -> float:
    max_average = -float("inf")
    for i in range(len(nums)):
        if i + k > len(nums):
            break
        if max_average < sum(nums[i : k + i]):
            max_average = sum(nums[i : k + i])
    return max_average / k


# 643. Maximum Average Subarray I (Sliding Window - O(n))
# Find a contiguous subarray of length k with the maximum average value.
def find_max_average(nums: list[int], k: int) -> float:
    # 1. Compute the sum of the very first window of size k
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # 2. Slide the window from index k to the end of the array
    for i in range(k, len(nums)):
        # Add the incoming element (nums[i]), drop the outgoing element (nums[i - k])
        current_sum += nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    # 3. Divide once at the end
    return max_sum / k


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer. Return true if there is a cycle, otherwise false.
def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head

    # Fast moves 2 steps, slow moves 1 step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If they meet, there is a cycle
        if slow == fast:
            return True

    # If fast hits None, the list ended (no cycle)
    return False


# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the
# index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, the left sum is 0 (likewise for right edge).
# Return the leftmost pivot index. If no such index exists, return -1.
def pivot_index(nums: list[int]) -> int:
    total_sum = sum(nums)  # O(n) once
    left_sum = 0

    for i, num in enumerate(nums):  # O(n) loop
        # Total minus left_sum minus current element gives the right sum in O(1)
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num  # O(1) running update

    return -1
    pass


# 20. Valid Parentheses (Template / Scratchpad)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
def is_valid(s: str) -> bool:
    # stack = []
    # Operations:
    # stack.append(x)  # Push  -> O(1) amortized
    # val = stack.pop()  # Pop   -> O(1)
    # top = stack[-1]  # Peek  -> O(1)
    # is_empty = not stack  # Check -> O(1)

    # Map closing brackets to their corresponding opening brackets
    matching = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If it's a closing bracket
        if char in matching:
            # Check if stack is non-empty and the top matches the corresponding opener
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
        else:
            # It's an opening bracket, push to stack
            stack.append(char)

    # Valid only if all opened brackets were successfully matched and popped
    return not stack


# 1047. Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. A duplicate removal consists
# of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
def remove_duplicates(s: str) -> str:
    stack = []

    for char in s:
        # If the stack has items and the top item matches the current char:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the adjacent duplicate pair
        else:
            stack.append(char)  # No match; push onto stack

    return "".join(stack)


# 1544. Make The String Great
# Given a string s of lower and upper case English letters. A good string is a string where
# no two adjacent characters s[i] and s[i + 1] satisfy:
# 0 <= i <= s.length - 2, s[i] is a lower-case letter and s[i + 1] is the same letter in upper-case
# or vice-versa. To make the string good, you can choose two adjacent letters that make the string
# bad and remove them. Return the string after making it good.
def make_good(s: str) -> str:
    stack = []
    for char in s:
        if stack and char != stack[-1] and char.lower() == stack[-1].lower():
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets```python
from collections import Counter, defaultdict, deque
import heapq


def main():
    print("Hello World")


# =====================================================================
# Problem: Two Sum
# Given an array of integers `nums` and an integer `target`, return indices
# of the two numbers such that they add up to `target`.
# Assume exactly one solution exists, and do not use the same element twice.
# =====================================================================
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []


# =====================================================================
# Problem: Valid Anagram
# Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
# and False otherwise (an anagram uses the exact same letters and counts).
# =====================================================================
# Approach 1: Counter comparison
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Approach 2: Manual frequency map
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1

    return True


# =====================================================================
# Problem: Contains Duplicate
# Given an integer array `nums`, return True if any value appears at least
# twice in the array, and return False if every element is distinct.
# =====================================================================
# Approach 1: Frequency count check
def contains_duplicate(nums: list[int]) -> bool:
    return any(count >= 2 for count in Counter(nums).values())


# Approach 2: Length comparison via set
def contains_duplicate(nums: list[int]) -> bool:
    # set drops duplicates unlike dictionary
    return len(nums) != len(set(nums))


# Approach 3: Early-exit lookup set
def contains_duplicate(nums: list[int]) -> bool:
    duplicates = set()
    for num in nums:
        if num in duplicates:
            return True
        duplicates.add(num)
    return False


# =====================================================================
# Problem: Best Time to Buy and Sell Stock
# Given an array `prices` where `prices[i]` is the price of a given stock
# on the i-th day, maximize profit by choosing a single day to buy and a
# different day in the future to sell. Return the maximum profit achievable.
# =====================================================================
def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# =====================================================================
# Problem: Valid Palindrome
# Given a string `s`, return True if it is a palindrome after converting
# all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters.
# =====================================================================
def is_palindrome(s: str) -> bool:
    n = ""
    for ch in s:
        if ch.isalnum():
            n += ch.lower()
    return n == n[::-1]


# =====================================================================
# Problem: Maximum Average Subarray I
# Given an integer array `nums` consisting of n elements and an integer `k`,
# find a contiguous subarray whose length is equal to `k` that has the
# maximum average value and return this value.
# =====================================================================
# Approach 1: Slicing - O(n * k)
def find_max_average(nums: list[int], k: int) -> float:
    max_average = -float("inf")
    for i in range(len(nums)):
        if i + k > len(nums):
            break
        if max_average < sum(nums[i : k + i]):
            max_average = sum(nums[i : k + i])
    return max_average / k


# Approach 2: Sliding Window - O(n)
def find_max_average(nums: list[int], k: int) -> float:
    # 1. Compute the sum of the very first window of size k
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # 2. Slide the window from index k to the end of the array
    for i in range(k, len(nums)):
        # Add incoming element (nums[i]), drop outgoing element (nums[i - k])
        current_sum += nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current