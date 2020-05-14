'''
Remove K Digits

Solution
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        nn = num
        for x in range(len(num)-1):
            l = 0
            if nn[x] >= nn[x+1]:
                nn = nn[0:x]+nn[x+1:]
                l += 1
            if l == k or len(int(nn)) == len(num)-1:
                return nn
        nn = []
        l = 0
        if len(num) == k:
        for x in range(len(num)-1):
            if num[x] > num[x+1]:
                nn.append(x)
                l += 1
            if l == k:
                break
        while l<k:
            nn.append(x+1)
            l += 1
            print('jjj')
        for x in nn[::-1]:
            num = num[:x] + num[x+1:]
        return num.lstrip('0') if num.lstrip('0') != '' else '0'
        '''
        s = []
        tempK = k
        for current in num:
            while k and s and s[-1] > current:
                s.pop()
                k -= 1
            s.append(current)
        ans = ''.join(s[:len(num)-tempK]).lstrip('0')
        if len(ans):
            return ans
        else:
            return '0'
