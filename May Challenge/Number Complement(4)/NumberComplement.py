'''
Number Complement

Solution
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:
'''

class Solution:
    def findComplement(self, num: int) -> int:
        tempBin = bin(num)
        otherBin = []
        for x in range(2,len(tempBin)):
            if tempBin[x] == '0':
                otherBin.append('1')
            else:
                otherBin.append('0')
        x = ''.join(otherBin)
        ans = int(x, 2)
        return ans

# Not necessary in leetcode env
s = Solution()
s.findComplement(5)
