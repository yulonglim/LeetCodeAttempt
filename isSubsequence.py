class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPt = 0
        tPt = 0
        for i in range(max(len(s),len(t))+1):
            if sPt == len(s):
                return True
            if tPt == len(t):
                return False
            if s[sPt] == t[tPt]:
                sPt += 1
            tPt += 1     
        return True 

if __name__ == "__main__":
    Solution = Solution()
    print(Solution.isSubsequence("fffff","ffffe"))