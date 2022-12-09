# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan&id=level-1

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == "__main__":
    Solution = Solution()
    print(Solution.isIsomorphic("paper","title"))