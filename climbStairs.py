# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        a = (1 + 5**(1/2))/2
        b = (1 - 5**(1/2))/2
        return int(((a**(n+1) - b**(n+1))/ (5**(1/2))))