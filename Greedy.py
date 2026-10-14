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