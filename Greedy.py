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
import heapq
from collections import deque, Counter
from itertools import count


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
"""
Problem: Minimum Meeting Rooms (Meeting Rooms II / LeetCode 253)
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required to hold all meetings.

Example 1:
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
Explanation:
- Room 1 hosts: [0, 30]
- Room 2 hosts: [5, 10], and can later host [15, 20] after [5, 10] ends.

Example 2:
Input: intervals = [[7, 10], [2, 4]]
Output: 1

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6
"""

from typing import List
import heapq


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    meeting_rooms = []
    for start, end in sorted_intervals:
        if meeting_rooms  and meeting_rooms[0] <= start:
            heapq.heappop(meeting_rooms)
        heapq.heappush(meeting_rooms,end)
    return len(meeting_rooms)

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
  """Example 1:

  Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
  Output: 1
  Explanation: [1, 3] can be removed and the rest of the intervals are
  non-overlapping.

  Example 2:
  Input: intervals = [[1, 2], [1, 2], [1, 2]]
  Output: 2

  Constraints:
  - 1 <= intervals.length <= 10^5
  - intervals[i].length == 2
  - -5 * 10^4 <= start_i < end_i <= 5 * 10^4
  """
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  removal = 0
  prev_end = sorted_intervals[0][1]
  for start, end in sorted_intervals[1:]:
      if start < prev_end:
          prev_end = min(prev_end, end)
          removal +=1
      else:
          prev_end = end
  return removal

from typing import List


def least_interval(tasks: List[str], n: int) -> int:
  """Example 1:

  Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
  Output: 8
  Explanation:
  A -> B -> idle -> A -> B -> idle -> A -> B
  Total time: 8.

  Example 2:
  Input: tasks = ["A", "C", "A", "B", "D", "B"], n = 1
  Output: 6
  Explanation: A -> B -> C -> D -> A -> B

  Constraints:
  - 1 <= tasks.length <= 10^4
  - tasks[i] is an uppercase English letter.
  - 0 <= n <= 100
  """
  from collections import Counter, deque
  import heapq

  def least_interval(tasks: list[str], n: int) -> int:
      counted_tasks = Counter(tasks)

      # Push negative counts so the largest count is at the top
      max_heap = [-cnt for cnt in counted_tasks.values()]
      heapq.heapify(max_heap)

      # Queue will store tuples of: (remaining_count, available_at_time)
      wait_queue = deque()
      time = 0

      while max_heap or wait_queue:
          time += 1

          # 1. Only pop from heap if there is a task ready to execute
          if max_heap:
              cnt = heapq.heappop(max_heap) + 1  # +1 because values are negative
              # Only enqueue if the task still has executions left (cnt < 0)
              if cnt != 0:
                  wait_queue.append((cnt, time + n))

          # 2. Check if a cooled-down task is ready to return to the heap
          if wait_queue and wait_queue[0][1] == time:
              ready_cnt, _ = wait_queue.popleft()
              heapq.heappush(max_heap, ready_cnt)

      return time

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
  """Example 1:

  Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
  Output: 2
  Explanation: The subarray [4, 3] has the minimal length under the problem
  constraints.

  Example 2:
  Input: target = 4, nums = [1, 4, 4]
  Output: 1

  Example 3:
  Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
  Output: 0

  Constraints:
  - 1 <= target <= 10^9
  - 1 <= nums.length <= 10^5
  - 1 <= nums[i] <= 10^4
  """
  if sum(nums) < target:
      return 0
  current_sum=0
  left = 0
  min_len = float('inf')
  for right in range(len(nums)):
      current_sum += nums[right]
      while current_sum >= target:
          min_len = min(min_len, right - left + 1)
          current_sum -= nums[left]
          left += 1
  if min_len == float('inf'):
      return 0
  return min_len

"""Example 1:

Input: target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30],
[60, 40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expend 10 fuel, and refuel 60 liters (tank = 60).
We drive to position 60, expend 50 fuel, refuel 40 liters (tank = 50).
We reach position 100 with 10 liters left.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10, 100]]
Output: -1
Explanation: We can't even reach the first station at position 10.

Constraints:
- 1 <= target, startFuel <= 10^9
- 0 <= stations.length <= 500
- 1 <= position_i < position_{i+1} < target
- 1 <= fuel_i <= 10^9
"""
from typing import List
import heapq

def min_refuel_stops(
      target: int, startFuel: int, stations: List[List[int]]
) -> int:
  # Max-Heap to store available fuel from passed stations (stored as negative values)
  max_fuel_heap = []

  current_fuel = startFuel
  stops = 0
  i = 0
  n = len(stations)

  while current_fuel < target:
      # 1. Drive forward and collect all stations reachable with our current fuel
      while i < n and stations[i][0] <= current_fuel:
          # Push fuel as negative to simulate a max-heap in Python
          heapq.heappush(max_fuel_heap, -stations[i][1])
          i += 1

      # 2. If we haven't reached target and have no stations to refuel from, we're stuck
      if not max_fuel_heap:
          return -1

      # 3. Greedily refuel at the station with the largest fuel capacity passed so far
      current_fuel += -heapq.heappop(max_fuel_heap)
      stops += 1

  return stops
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
]
# Output: 5
# Explanation: The connected cluster of 1's starting around (0,2), (1,1), (1,2), (2,1), (2,2) has area 5.
grid2 = [
    [0, 0, 0],
    [0, 0, 0],
]
# Output: 0

def largest_corrosion_patch(grid: list[list[int]]) -> int:
  visited = set()
  max_corrosion = 0

  def dfs(r: int, c: int) -> int:
    # 1. Boundary & Base checks first:
    if (
        r < 0
        or r >= len(grid)
        or c < 0
        or c >= len(grid[0])
        or (r, c) in visited
        or grid[r][c] == 0
    ):
      return 0

    # 2. Mark this cell visited:
    visited.add((r, c))

    # 3. Sum 1 (this cell) + all 4 directions:
    return (
        1
        + dfs(r - 1, c)  # up
        + dfs(r + 1, c)  # down
        + dfs(r, c - 1)  # left
        + dfs(r, c + 1)  # right
    )

  # 4. Traverse every cell on the inspection surface
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 1 and (r, c) not in visited:
        current_patch_size = dfs(r, c)
        max_corrosion = max(max_corrosion, current_patch_size)

  return max_corrosion

def has_critical_anomaly(
    readings: list[list[float]], window_size: int, k: int, threshold: float
) -> bool:
  anomaly = []
  for i in range(len(readings)):
       reading = readings[i]
       if reading[1]< threshold:
           anomaly.append(reading[0])
  for i in range(len(anomaly) - k + 1):
      if anomaly[i + k - 1] - anomaly[i] <= window_size:
          return True
  return False


def find_inspection_gaps(
    passes: list[list[float]], pipe_length: float
) -> list[list[float]]:
   passes = sorted(passes,key=lambda x: x[0])
   current_reach = 0.0
   array = []
   for start, end in passes:
       if start - current_reach > 0:
           unchecked = [current_reach,start]
           array.append(unchecked)
       current_reach = max(current_reach,end)
   if current_reach < pipe_length:
       array.append([current_reach, pipe_length])
   return array






