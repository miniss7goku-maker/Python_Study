from collections import Counter, defaultdict, deque

# =====================================================================
# Common Data Structures
# =====================================================================


class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# =====================================================================
# LC 79: Word Search
# =====================================================================
# Problem Statement:
# Given an m x n grid of characters 'board' and a string 'word', return
# True if 'word' exists in the grid. The word can be constructed from
# letters of sequentially adjacent cells (horizontally or vertically
# neighboring). The same letter cell may not be used more than once.
#
# Time Complexity:  O(m * n * 4^L) - Where L is len(word).
# Space Complexity: O(L) - Recursion call stack depth.
# =====================================================================
def exist(board: list[list[str]], word: str) -> bool:
  ROWS, COLS = len(board), len(board[0])

  def dfs(r: int, c: int, k: int) -> bool:
    if k == len(word):
      return True

    if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[k]:
      return False

    temp = board[r][c]
    board[r][c] = "#"

    found = (
        dfs(r + 1, c, k + 1)
        or dfs(r - 1, c, k + 1)
        or dfs(r, c + 1, k + 1)
        or dfs(r, c - 1, k + 1)
    )

    board[r][c] = temp
    return found

  for r in range(ROWS):
    for c in range(COLS):
      if board[r][c] == word[0] and dfs(r, c, 0):
        return True

  return False


# =====================================================================
# LC 5: Longest Palindromic Substring
# =====================================================================
# Problem Statement:
# Given a string 's', return the longest palindromic substring in 's'.
#
# Time Complexity:  O(n^2) - Expand around center across n centers.
# Space Complexity: O(1) - Constant auxiliary space.
# =====================================================================
def longest_palindrome(s: str) -> str:
  if len(s) < 2:
    return s

  def expand(left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return s[left + 1 : right]

  longest = ""
  for i in range(len(s)):
    odd = expand(i, i)
    even = expand(i, i + 1)

    if len(odd) > len(longest):
      longest = odd
    if len(even) > len(longest):
      longest = even

  return longest


# =====================================================================
# LC 11: Container With Most Water
# =====================================================================
# Problem Statement:
# Given an integer array 'height' of length n, where each index
# represents a vertical line drawn at coordinate (i, height[i]).
# Find two lines that together with the x-axis form a container, such
# that the container contains the most water. Return the maximum area.
#
# Time Complexity:  O(n) - Single pass with two pointers.
# Space Complexity: O(1) - Auxiliary pointers only.
# =====================================================================
def max_area(height: list[int]) -> int:
  left = 0
  right = len(height) - 1
  max_water = 0

  while left < right:
    width = right - left
    h = min(height[left], height[right])
    max_water = max(max_water, width * h)

    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return max_water


# =====================================================================
# LC 42: Trapping Rain Water
# =====================================================================
# Problem Statement:
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.
#
# Time Complexity:  O(n) - Two-pointer sweep.
# Space Complexity: O(1) - In-place tracking without precomputed arrays.
# =====================================================================
def trap(height: list[int]) -> int:
  if not height:
    return 0

  left = 0
  right = len(height) - 1
  left_max = 0
  right_max = 0
  total_water = 0

  while left < right:
    if height[left] < height[right]:
      if height[left] >= left_max:
        left_max = height[left]
      else:
        total_water += left_max - height[left]
      left += 1
    else:
      if height[right] >= right_max:
        right_max = height[right]
      else:
        total_water += right_max - height[right]
      right -= 1

  return total_water


# =====================================================================
# LC 875: Koko Eating Bananas
# =====================================================================
# Problem Statement:
# Koko loves to eat bananas. There are n piles of bananas, the i-th pile
# has 'piles[i]' bananas. The guards will come back in 'h' hours.
# Return the minimum integer 'k' such that she can eat all bananas within 'h' hours.
#
# Time Complexity:  O(n * log(max(piles))) - Binary search on answer space.
# Space Complexity: O(1) - Constant auxiliary space.
# =====================================================================
def min_eating_speed(piles: list[int], h: int) -> int:
  if len(piles) > h:
    return -1
  if len(piles) == h:
    return max(piles)

  low = max(1, (sum(piles) + h - 1) // h)
  high = max(piles)

  def can_finish(speed: int) -> bool:
    total_hours = 0
    for pile in piles:
      total_hours += (pile + speed - 1) // speed
      if total_hours > h:
        return False
    return True

  while low < high:
    mid = low + (high - low) // 2
    if can_finish(mid):
      high = mid
    else:
      low = mid + 1

  return low


# =====================================================================
# LC 1011: Capacity To Ship Packages Within D Days
# =====================================================================
# Problem Statement:
# Contiguous packages with weights 'weights[i]' must be shipped within 'days' days.
# Return the least capacity of the ship that allows all packages to be shipped.
#
# Time Complexity:  O(n * log(sum(weights) - max(weights)))
# Space Complexity: O(1) - Constant space.
# =====================================================================
def ship_within_days(weights: list[int], days: int) -> int:
  low = max(weights)
  high = sum(weights)

  def can_ship(capacity: int) -> bool:
    days_needed = 1
    current_load = 0

    for w in weights:
      if current_load + w > capacity:
        days_needed += 1
        current_load = 0
      current_load += w

      if days_needed > days:
        return False
    return True

  while low < high:
    mid = low + (high - low) // 2
    if can_ship(mid):
      high = mid
    else:
      low = mid + 1

  return low


# =====================================================================
# LC 167: Two Sum II - Input Array Is Sorted
# =====================================================================
# Problem Statement:
# Given a 1-indexed array of integers 'numbers' sorted in non-decreasing order,
# find two numbers such that they add up to a specific 'target' number.
# Return the 1-based indices [index1, index2].
#
# Time Complexity:  O(n) - Two-pointer squeeze.
# Space Complexity: O(1) - Strict O(1) memory bound.
# =====================================================================
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
  left = 0
  right = len(numbers) - 1

  while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
      return [left + 1, right + 1]
    elif current_sum > target:
      right -= 1
    else:
      left += 1

  return []


# =====================================================================
# LC 739: Daily Temperatures
# =====================================================================
# Problem Statement:
# Return an array 'answer' such that 'answer[i]' is the number of days you
# have to wait after the i-th day to get a warmer temperature.
#
# Time Complexity:  O(n) - Each day index pushed/popped at most once.
# Space Complexity: O(n) - Monotonic stack auxiliary storage.
# =====================================================================
def daily_temperatures(temperatures: list[int]) -> list[int]:
  stack = []
  answer = [0] * len(temperatures)

  for i, temp in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < temp:
      old_index = stack.pop()
      answer[old_index] = i - old_index
    stack.append(i)

  return answer


# =====================================================================
# LC 3: Longest Substring Without Repeating Characters
# =====================================================================
# Problem Statement:
# Given a string 's', find the length of the longest substring
# without duplicate characters.
#
# Time Complexity:  O(n) - Single pass through the string with sliding window.
# Space Complexity: O(min(n, m)) - Hash map bounded by alphabet size m.
# =====================================================================
def length_of_longest_substring(s: str) -> int:
  if not s:
    return 0

  char_map = {}
  left = 0
  max_length = 0

  for i, char in enumerate(s):
    if char in char_map:
      left = max(left, char_map[char] + 1)

    char_map[char] = i
    max_length = max(max_length, i - left + 1)

  return max_length


# =====================================================================
# LC 424: Longest Repeating Character Replacement
# =====================================================================
# Problem Statement:
# Given a string 's' and an integer 'k', find the length of the longest
# substring containing the same letter after replacing at most 'k' characters.
#
# Time Complexity:  O(n) - Sliding window where pointers only advance.
# Space Complexity: O(1) - Upper bound of 26 uppercase letters.
# =====================================================================
def character_replacement(s: str, k: int) -> int:
  if not s:
    return 0

  counts = {}
  left = 0
  max_freq = 0
  max_len = 0

  for right, char in enumerate(s):
    counts[char] = counts.get(char, 0) + 1
    max_freq = max(max_freq, counts[char])

    while (right - left + 1) - max_freq > k:
      counts[s[left]] -= 1
      left += 1

    max_len = max(max_len, right - left + 1)

  return max_len


# =====================================================================
# LC 76: Minimum Window Substring
# =====================================================================
# Problem Statement:
# Return the minimum window substring of 's' such that every character in 't'
# (including duplicates) is included in the window. Return "" if none exists.
#
# Time Complexity:  O(m + n) - Each character visited at most twice.
# Space Complexity: O(|Sigma|) - Bounded by alphabet size.
# =====================================================================
def min_window(s: str, t: str) -> str:
  if not s or not t or len(s) < len(t):
    return ""

  req_counts = Counter(t)
  window_counts = {}
  formed = 0
  required = len(req_counts)

  min_len = float("inf")
  best_range = (0, 0)
  left = 0

  for right, char in enumerate(s):
    if char in req_counts:
      window_counts[char] = window_counts.get(char, 0) + 1
      if window_counts[char] == req_counts[char]:
        formed += 1

    while formed == required:
      current_len = right - left + 1
      if current_len < min_len:
        min_len = current_len
        best_range = (left, right + 1)

      left_char = s[left]
      if left_char in req_counts:
        if window_counts[left_char] == req_counts[left_char]:
          formed -= 1
        window_counts[left_char] -= 1

      left += 1

  return s[best_range[0] : best_range[1]] if min_len != float("inf") else ""


# =====================================================================
# LC 206: Reverse Linked List
# =====================================================================
# Problem Statement:
# Given the head of a singly linked list, reverse the list, and return
# the reversed list's head.
#
# Time Complexity:  O(n) - Single pass through all nodes.
# Space Complexity: O(1) - Pointer manipulation in-place.
# =====================================================================
def reverse_list(head: ListNode | None) -> ListNode | None:
  prev = None
  curr = head

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

  return prev


# =====================================================================
# LC 143: Reorder List
# =====================================================================
# Problem Statement:
# Reorder a singly linked list in-place to: L0 -> Ln -> L1 -> Ln-1 -> ...
# Do not modify node values or return anything.
#
# Time Complexity:  O(n) - Split, reverse second half, weave.
# Space Complexity: O(1) - In-place pointer updates.
# =====================================================================
def reorder_list(head: ListNode | None) -> None:
  if not head or not head.next:
    return

  # 1. Find midpoint (slow lands on midpoint/left-mid)
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # 2. Split and reverse second half
  second = slow.next
  slow.next = None

  prev = None
  curr = second
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  # 3. Interleave first and reversed second half
  first = head
  second = prev
  while second:
    tmp1 = first.next
    tmp2 = second.next

    first.next = second
    second.next = tmp1

    first = tmp1
    second = tmp2


# =====================================================================
# LC 226: Invert Binary Tree
# =====================================================================
# Problem Statement:
# Given the root of a binary tree, invert the tree, and return its root.
#
# Time Complexity:  O(n) - Visits every node once.
# Space Complexity: O(h) - Call stack bounded by tree height h.
# =====================================================================
def invert_tree(root: TreeNode | None) -> TreeNode | None:
  if not root:
    return None

  root.left, root.right = root.right, root.left
  invert_tree(root.left)
  invert_tree(root.right)

  return root


# =====================================================================
# LC 104: Maximum Depth of Binary Tree
# =====================================================================
# Problem Statement:
# Given the root of a binary tree, return its maximum depth along the
# longest path from root down to the farthest leaf node.
# =====================================================================

# Variant A: Iterative BFS (Level-Order Queue)
# Time Complexity:  O(n) - Visits each node once.
# Space Complexity: O(w) - Bounded by maximum tree width w (at most ~n/2).
def max_depth_bfs(root: TreeNode | None) -> int:
  if not root:
    return 0

  queue = deque([root])
  depth = 0

  while queue:
    for _ in range(len(queue)):
      node = queue.popleft()
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    depth += 1

  return depth


# Variant B: Recursive DFS (Post-Order Traversal)
# Time Complexity:  O(n) - Visits each node once.
# Space Complexity: O(h) - Auxiliary stack frames bounded by height h.
def max_depth_dfs(root: TreeNode | None) -> int:
  if not root:
    return 0

  return 1 + max(max_depth_dfs(root.left), max_depth_dfs(root.right))

# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
  """Returns the level-order traversal of a binary tree's values.

  Do not show full solution directly.
  """
  if not root:
      return []
  result = []
  queue = deque([root])
  while queue:
      levelvalues =  []
      for _ in range(len(queue)):
          node = queue.popleft()
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
          levelvalues.append(node.val)
      result.append(levelvalues)
  return result

# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)  # Snapshot the number of nodes on this level

        for i in range(level_size):
            node = queue.popleft()

            # The last element popped in this row is visible from the right
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
from collections import defaultdict, deque

# =====================================================================
# PROBLEM 1: Total Team Salary (Organizational Hierarchy BFS)
# =====================================================================
"""
PROBLEM: Calculate Total Team Salary Under a Target Employee

Given an organizational chart represented by a list of Employee objects,
calculate the cumulative salary of a specific target employee and all
of their direct and indirect subordinates (the entire sub-tree).

Requirements:
- Each employee has an id, name, salary, and list of direct_report IDs.
- If the target employee ID is not present or the list is empty, return 0.
- Traverse all levels down the management hierarchy.

Complexity:
- Time: O(N) where N is the total number of employees.
- Space: O(N) to store the ID lookup map and BFS queue.
"""


class Employee:

  def __init__(
      self,
      id: int,
      name: str,
      salary: int,
      direct_reports: list[int] | None = None,
  ):
    self.id = id
    self.name = name
    self.salary = salary
    self.direct_reports = direct_reports if direct_reports is not None else []


def total_team_salary(Employees: list[Employee] | None, target_id: int) -> int:
  if not Employees:
    return 0

  # O(N) lookup map so we don't scan the list repeatedly
  emp_map = {emp.id: emp for emp in Employees}

  if target_id not in emp_map:
    return 0

  total_salary = 0
  queue = deque([target_id])

  # Standard BFS traversal down the reporting tree
  while queue:
    curr_id = queue.popleft()
    curr_emp = emp_map[curr_id]

    total_salary += curr_emp.salary

    # Push all direct subordinates onto the queue
    for report_id in curr_emp.direct_reports:
      if report_id in emp_map:
        queue.append(report_id)

  return total_salary


# =====================================================================
# PROBLEM 2: Sensor Thickness Anomaly Aggregation (Merge Intervals)
# =====================================================================
"""
PROBLEM: Sensor Thickness Anomaly Aggregation

A Gecko inspection crawler scans the steel wall of a storage tank along a 1D track.
As it drives, it flags regions where the metal wall thickness falls below safety standards.
Each flagged region is reported as an interval: [start_pos_cm, end_pos_cm].

Because multiple sensors run concurrently, the recorded defect regions often overlap 
or are immediately adjacent.

Write a function `consolidate_defects(intervals: list[list[int]]) -> list[list[int]]` 
that merges all overlapping or contiguous defect regions and returns the consolidated 
list sorted by starting position.

Example 1:
    Input:  intervals = [[10, 30], [20, 50], [80, 100], [90, 120]]
    Output: [[10, 50], [80, 120]]
    Explanation: [10, 30] and [20, 50] overlap -> [10, 50]. 
                 [80, 100] and [90, 120] overlap -> [80, 120].

Example 2:
    Input:  intervals = [[15, 25], [25, 40]]
    Output: [[15, 40]]
    Explanation: Adjacent endpoints touch, so they consolidate.

Constraints:
- 0 <= len(intervals) <= 10^4
- interval[0] <= interval[1]
"""


def consolidate_defects(intervals: list[list[int]]) -> list[list[int]]:
  if not intervals:
    return []

  # Sort by starting point
  intervals.sort(key=lambda x: x[0])

  consolidated = [intervals[0]]

  for current in intervals[1:]:
    prev = consolidated[-1]

    # Touching (prev[1] >= current[0]) or overlapping
    if current[0] <= prev[1]:
      prev[1] = max(prev[1], current[1])
    else:
      consolidated.append(current)

  return consolidated


# =====================================================================
# PROBLEM 3: Travel Advisor Commission & Booking Summary
# =====================================================================
"""
PROBLEM: Travel Advisor Commission & Booking Summary

Process raw booking records to generate an aggregated performance report per advisor.

Requirements:
1. Filter: Include only records where status == "completed".
2. Aggregation per Advisor:
   - total_commission: Sum of completed commission amounts, rounded to 2 decimal places.
   - completed_trips: Count of completed bookings.
   - top_destination: Destination with highest completed count; if tied, pick alphabetically earlier destination.
3. Sort Order:
   - Descending by total_commission.
   - Tie-break: Ascending (alphabetical) by advisor_id.

Input Schema:
    bookings = [
        {"advisor_id": str, "destination": str, "commission": float, "status": str}
    ]
"""


def generate_advisor_report(bookings: list[dict]) -> list[dict]:
  if not bookings:
    return []

  # advisor_id -> {"total_commission": float, "completed_trips": int, "destinations": {dest: count}}
  advisor_map = {}

  # Loop 1: Accumulate completed stats
  for booking in bookings:
    if booking.get("status") != "completed":
      continue

    adv_id = booking["advisor_id"]
    dest = booking["destination"]
    comm = booking.get("commission", 0.0)

    if adv_id not in advisor_map:
      advisor_map[adv_id] = {
          "total_commission": 0.0,
          "completed_trips": 0,
          "destinations": {},
      }

    data = advisor_map[adv_id]
    data["total_commission"] += comm
    data["completed_trips"] += 1
    data["destinations"][dest] = data["destinations"].get(dest, 0) + 1

  # Loop 2: Format and resolve tie-break for top destination
  report = []
  for adv_id, data in advisor_map.items():
    # Sort destination keys alphabetically first, then pick the max count (stable max preserves alphabetical order)
    best_destinations = sorted(data["destinations"].keys())
    top_dest = max(best_destinations, key=lambda d: data["destinations"][d])

    report.append({
        "advisor_id": adv_id,
        "total_commission": round(data["total_commission"], 2),
        "completed_trips": data["completed_trips"],
        "top_destination": top_dest,
    })

  # Sort descending by commission, tie-break by advisor_id ascending
  report.sort(key=lambda x: (-x["total_commission"], x["advisor_id"]))
  return report


# =====================================================================
# PROBLEM 4: Hotel Room Availability & Payout Aggregator
# =====================================================================
"""
PROBLEM: Hotel Room Availability & Payout Aggregator

Detect room collisions and calculate total supplier payouts for valid bookings.

Requirements:
1. Group reservations by room_id and sort chronologically by check_in day.
2. Detect overlaps on half-open intervals [check_in, check_out):
   - Overlap occurs strictly if: next_check_in < current_check_out.
   - Same-day turnaround (next_check_in == current_check_out) is valid (no conflict).
3. Financial & Room tracking:
   - Payout per valid reservation: (check_out - check_in) * nightly_rate.
   - Keep conflicting reservation IDs.
   - Track unique room IDs that fulfilled at least one valid reservation.
4. Return dictionary:
   - valid_payout_total: float rounded to 2 decimal places.
   - conflicted_reservation_ids: sorted list of conflicting res_id strings.
   - rooms_utilized: sorted list of unique room_id strings.
"""


def process_room_bookings(reservations: list[dict]) -> dict:
  if not reservations:
    return {
        "valid_payout_total": 0.0,
        "conflicted_reservation_ids": [],
        "rooms_utilized": [],
    }

  # Group by room_id
  room_map = defaultdict(list)
  for res in reservations:
    room_map[res["room_id"]].append(res)

  valid_payout = 0.0
  conflicted_ids = []
  valid_rooms = set()

  # Process each room's timeline independently
  for room_id, bookings in room_map.items():
    bookings.sort(key=lambda r: r["check_in"])
    last_checkout = -1

    for b in bookings:
      check_in = b["check_in"]
      check_out = b["check_out"]

      # Strict overlap check for half-open intervals
      if check_in < last_checkout:
        conflicted_ids.append(b["res_id"])
      else:
        last_checkout = check_out
        nights = check_out - check_in
        valid_payout += nights * b.get("nightly_rate", 0.0)
        valid_rooms.add(room_id)

  conflicted_ids.sort()
  sorted_rooms = sorted(valid_rooms)

  return {
      "valid_payout_total": round(valid_payout, 2),
      "conflicted_reservation_ids": conflicted_ids,
      "rooms_utilized": sorted_rooms,
  }


# =====================================================================
# PROBLEM 5: Peak Booking Window Detector (Sliding Window)
# =====================================================================
"""
PROBLEM: Peak Booking Window Detector

Given a list of daily booking counts and a window size k, find the continuous
k-day window with the highest total bookings.

Requirements:
- Window size k is contiguous.
- If multiple windows tie for max bookings, return the earliest start_index.
- If k <= 0, k > len(daily_counts), or daily_counts is empty, return {"max_bookings": 0, "start_index": -1}.

Complexity:
- Time: O(N) using an O(1) sliding window sum update.
- Space: O(1) auxiliary space.
"""


def find_peak_booking_window(daily_counts: list[int], k: int) -> dict:
  if not daily_counts or k <= 0 or k > len(daily_counts):
    return {"max_bookings": 0, "start_index": -1}

  # 1. Initialize first window sum
  current_sum = sum(daily_counts[:k])
  max_sum = current_sum
  best_start = 0

  # 2. Slide the window in O(1) per step
  for i in range(k, len(daily_counts)):
    current_sum += daily_counts[i] - daily_counts[i - k]

    # Strictly greater preserves earliest start index on ties
    if current_sum > max_sum:
      max_sum = current_sum
      best_start = i - k + 1

  return {"max_bookings": max_sum, "start_index": best_start}


"""
PROBLEM: In-Place Merge Sorted Arrays (3-Pointer Backward Fill)

Given two sorted integer arrays, nums1 and nums2, merge nums2 into nums1 
in-place as one sorted array.

Constraints:
- nums1 has a total length of m + n (m valid elements + n dummy slots).
- nums2 has a total length of n (n valid elements).
- Time Complexity: O(m + n)
- Space Complexity: O(1) auxiliary space (modify nums1 in place).
"""


def merge_unsorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    nums1: [2, 5, 6, 5, 5, 5], m = 3
    nums2: [1, 4, 2], n = 3
    """
    # Overwrite dummy slots [m : m+n] with nums2
    for i in range(n):
        nums1[m + i] = nums2[i]

    # In-place sort (Timsort: O(1) auxiliary user space)
    nums1.sort()
    return nums1


# Test
nums1 = [2, 5, 6, 5, 5, 5]
nums2 = [1, 4, 2]
print(merge_unsorted_arrays(nums1, 3, nums2, 3))


def merge_unsorted_linear_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    # Step 1: Overwrite dummy slots with nums2 -> O(N)
    for i in range(n):
        nums1[m + i] = nums2[i]

    total_len = m + n  # 2 * N
    i = 0

    # Step 2: Cycle sort in-place -> O(N) time, O(1) auxiliary space
    while i < total_len:
        correct_idx = nums1[i] - 1  # For 1-indexed values (1 -> idx 0, 2 -> idx 1, etc.)

        # If the number is in valid range and not already in its correct spot
        if 0 <= correct_idx < total_len and nums1[i] != nums1[correct_idx]:
            # Swap to correct position
            nums1[i], nums1[correct_idx] = nums1[correct_idx], nums1[i]
        else:
            i += 1

    return nums1


# Test
nums1 = [2, 5, 6, 5, 5, 5]
nums2 = [1, 4, 2]
print(merge_unsorted_linear_inplace(nums1, 3, nums2, 3))
# Output: [1, 2, 2, 4, 5, 6]
# Output: [1, 2, 2, 4, 5, 6]
def count_target_windows(transactions: list[int], target: int) -> int:
    # Map prefix_sum -> count of times seen
    # Base case: a prefix sum of 0 has occurred once before processing any elements
    prefix_counts = {0: 1}
    curr_sum = 0
    total_matches = 0

    for x in transactions:
        curr_sum += x
        diff = curr_sum - target

        # If (curr_sum - target) exists in our map, add its frequency
        if diff in prefix_counts:
            total_matches += prefix_counts[diff]

        # Record or increment the current prefix sum
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return total_matches
import heapq
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    map = []
    for start, end in intervals:
        # If the earliest ending meeting finishes at or before the current start time, reuse that room
        if map and map[0] <= start:
            heapq.heappop(map)

        # Allocate room (or push updated end time)
        heapq.heappush(map, end)

        # Size of the heap equals the max concurrent rooms needed
    return len(map)

def is_valid_expression(s: str) -> bool:
    # Map closing delimiter -> expected opening delimiter
    matching = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If it's an opening delimiter, push to stack
        if char in matching.values():
            stack.append(char)
        # If it's a closing delimiter, validate and pop
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        # Any non-bracket characters (e.g., numbers, operators) are ignored

    # Valid only if all opened pairs were closed
    return len(stack) == 0
def count_exposure_clusters(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    clusters = 0

    def dfs(r: int, c: int) -> None:
        # Base termination: bounds check or non-cluster cell
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        # Sink the cell in-place to avoid needing an extra visited set
        grid[r][c] = "0"

        # Explore all 4 orthogonal directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Outer loop drives traversal across every grid coordinate
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                clusters += 1  # Found a new cluster
                dfs(r, c)      # Visit and sink every connected '1'

    return clusters
"""
Problem: Group Anagrams / Transaction Reconciliation
Given an array of transaction code strings `strs`, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    if not strs:
        return []
    map = {
    }
    for s in strs:
        tup = tuple(sorted(s))
        if tup in map:
            map[tup].append(s)
        else:
            map[tup] = [s]
    return list(map.values())
    from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    if not strs:
        return []

    anagram_map = defaultdict(list)
    for s in strs:
        anagram_map[tuple(sorted(s))].append(s)

    return list(anagram_map.values())
"""
Problem: Merge Overlapping Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4
"""

"""
Problem: Merge Overlapping Intervals
Given an array of intervals where intervals[i] = [start_i, end_i], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # 1. Chronological sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = []

    for start, end in intervals:
        # Case 1: First interval OR non-overlapping gap
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        # Case 2: Overlapping interval -> stretch previous end boundary
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged
    pass
# =====================================================================
# Test Suite
# =====================================================================
if __name__ == "__main__":

  def list_to_array(node: ListNode | None) -> list[int]:
    out = []
    while node:
      out.append(node.val)
      node = node.next
    return out

  def array_to_list(arr: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
      curr.next = ListNode(v)
      curr = curr.next
    return dummy.next

  # String & Array assertions
  board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
  assert exist(board, "ABCCED") is True
  assert longest_palindrome("babad") in ("bab", "aba")
  assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
  assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
  assert min_eating_speed([3, 6, 7, 11], 8) == 4
  assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
  assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
  assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
      1,
      1,
      4,
      2,
      1,
      1,
      0,
      0,
  ]
  assert length_of_longest_substring("abcabcbb") == 3
  assert character_replacement("AABABBA", 1) == 4
  assert min_window("ADOBECODEBANC", "ABC") == "BANC"

  # Linked List assertions
  l1 = array_to_list([1, 2, 3, 4, 5])
  rev = reverse_list(l1)
  assert list_to_array(rev) == [5, 4, 3, 2, 1]

  l2 = array_to_list([1, 2, 3, 4, 5])
  reorder_list(l2)
  assert list_to_array(l2) == [1, 5, 2, 4, 3]

  # Binary Tree assertions
  # Build Tree: [3, 9, 20, None, None, 15, 7]
  tree = TreeNode(3)
  tree.left = TreeNode(9)
  tree.right = TreeNode(20, TreeNode(15), TreeNode(7))

  assert max_depth_bfs(tree) == 3
  assert max_depth_dfs(tree) == 3

  invert_tree(tree)
  assert tree.left.val == 20
  assert tree.right.val == 9
  assert tree.left.left.val == 7
  assert tree.left.right.val == 15

  print("All assertions passed successfully.")