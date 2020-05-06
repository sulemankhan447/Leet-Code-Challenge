'''
First Unique Character in a String

Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in range(len(s)):
            if s.count(s[x])> 1:
                continue
            else:
                return x
        return -1

s=Solution()
s.firstUniqChar("leetcode")
