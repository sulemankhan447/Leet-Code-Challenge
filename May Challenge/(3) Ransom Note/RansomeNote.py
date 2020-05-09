'''
Ransom Note

Solution
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

class Solution:
    def canConstruct(self, ransomNote, magazine):
        flag = 0
        for x in range(len(ransomNote)):
            if(ransomNote.count(ransomNote[x]) <= magazine.count(ransomNote[x])):
                continue
            else:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False

#Not necessary in leetcode env
a = Solution()
print(a.canConstruct("a", "b"))
print(a.canConstruct("aa", "ab"))
print(a.canConstruct("aa", "aab"))
