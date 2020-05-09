'''
Jewels and Stones Solution

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

def removeDuplicates(string):
    uniqs = ''
    for x in string:
        if not (x in uniqs):
            uniqs = uniqs + x
    return uniqs

class Solution:
    def numJewelsInStones(self, J, S) :
        # jlen = len(J)
        # slen = len(S)
        # if slen>jlen:
        #     length = slen
        # else:
        #     length = jlen
        tot = 0
        J = removeDuplicates(J)
        for x in range(len(J)):
            temp = J[x]
            if temp in S:
                tot += S.count(temp)
        return tot

#Not Necessary in leetcode env
a = Solution() 
print(a.numJewelsInStones('aAAB','aAABBB'))
