from typing import List, Optional
from collections import Counter, deque
import math


class Solution:
    def interpret(self,command:str)->str:
        return command.replace("()","o").replace("()","al")

class Solution2:
    def destCity(self, paths: List[List[str]]) -> List[str]:
        dict ={}
        for path in paths:
            city_a,city_b = path
            dict[city_a]=dict.get(city_a,0)+1
            dict[city_b]=dict.get(city_b,0)
        for city in dict:
            if dict[city]==0:
                return city

    def destCity2(self, paths: List[List[str]]) -> List[str]:
        # Collect all starting cities into a set (hashable and fast lookup)
        start_cities = {path[0] for path in paths}

        # Find the destination city that never acts as a starting city
        for path in paths:
            dest = path[1]
            if dest not in start_cities:
                return dest


class Solution3(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=sorted(nums, reverse=True)
        value_dict = {}
        newnums = []
        for i in range(len(li)-1):
            curnum = li[i]
            next_num = li[i+1]
            if next_num < curnum:
                remainder = len(li)-(i+1)
                value_dict[curnum] =  remainder
        value_dict[li[-1]] = 0
        output =[]
        for num in nums:
            output.append(value_dict[num])
        return output


class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Find the exact midpoint index
            mid = (left + right) // 2

            # Case 1: Found the target! Return its index.
            if nums[mid] == target:
                return mid

            # Case 2: Target is smaller, discard the right half
            elif nums[mid] > target:
                right = mid - 1

            # Case 3: Target is larger, discard the left half
            else:
                left = mid + 1

        # If the loop finishes without returning, the target isn't in the list
        return -1

    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: int
            """
            char_count= {}
            for char in s:
                    char_count[char] = char_count.get(char,0)+1
            final_count = 0
            odd_is_present =False
            for char in char_count:
                if char_count[char]% 2 ==0:
                    final_count += char_count[char]
                else:
                    final_count += char_count[char]-1
                    odd_is_present=True
            if odd_is_present:
                final_count +=1
            return final_count


class Solution(object):
    def maxCoins(self, piles:int):
        """
        :type piles: List[int]
        :rtype: int
        """
        val=sorted(piles, reverse=True)
        end_index = len(val)-1
        our_value = 0
        for i in range(len(val)//3):
            our_value += val[end_index-(i*2)-1]
        return our_value


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.current_index += 1
        self.history = self.history[0:self.current_index]
        self.history.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index = max(0,self.current_index - steps)
        return self.history[self.current_index]
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index = (len(self.history)-1, self.current_index+steps)
        return self.history[self.current_index]


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Convert to a set for O(1) lightning-fast lookups
        to_delete_set = set(to_delete)
        output = []

        def dfs(node, is_root):
            if not node:
                return None

            # Check if this specific node needs to be deleted
            deleted = node.val in to_delete_set

            # If it's a standalone root and NOT deleted, add it to our forest
            if is_root and not deleted:
                output.append(node)

            # Post-order: Process children first, passing whether they will become new roots
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            # Return None to the parent if this node is deleted, severing the link cleanly
            return None if deleted else node

        # The initial root node starts with is_root = True
        dfs(root, True)
        return output

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        # 1. Convert to a set for fast O(1) lookups
        to_delete_set = set(to_delete)
        output = []

        # 2. Queue stores tuples: (current_node, is_root_flag)
        # The initial root node starts with is_root = True
        queue = deque([(root, True)])

        while queue:
            node, is_root = queue.popleft()

            # Check if this node is slated for deletion
            deleted = node.val in to_delete_set

            # If it's a valid root and not deleted, it belongs in our forest
            if is_root and not deleted:
                output.append(node)

            # Process Left Child
            if node.left:
                # If current node is deleted, the child becomes a new root candidate
                queue.append((node.left, deleted))
                # Disconnect the link immediately if the child itself needs to be deleted
                if node.left.val in to_delete_set:
                    node.left = None

            # Process Right Child
            if node.right:
                # If current node is deleted, the child becomes a new root candidate
                queue.append((node.right, deleted))
                # Disconnect the link immediately if the child itself needs to be deleted
                if node.right.val in to_delete_set:
                    node.right = None

        return output

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



