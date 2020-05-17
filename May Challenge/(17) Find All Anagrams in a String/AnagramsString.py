'''
Find All Anagrams in a String

Solution
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
#Sort
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_length = len(p)
        s_length = len(s)
        pp = sorted(p)
        final = []
        for x in range(s_length-p_length+1):
            temp = s[x:x+p_length]
            temp = sorted(temp)
            if temp == pp:
                final.append(x)
        return final

'''

# Solution 1 : Sliding Window, Hash Table
    def findAnagrams(self, s, p):
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            if i == 0: cnt_s = Counter(s[:m])
            else:
                prev = s[i-1]; curr = s[i+m-1]
                cnt_s[prev] -= 1; cnt_s[curr] += 1
                if cnt_s[prev] == 0: del cnt_s[prev]
            if cnt_s == cnt_p: res.append(i)
        return res        
        
		
# Solution 2 : Hash Table
    def findAnagrams2(self, s, p):
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            cnt_s = Counter(s[i:i+m])
            if cnt_s == cnt_p: res.append(i)
        return res 

'''
