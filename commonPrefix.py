# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dic = {}
        word1 = strs[0]
        prefix = ""
        for char in word1:
            prefix += char
            dic[prefix] = 1
        for word in strs[1:]:
            prefix = ""
            for char in word:
                prefix += char
                if prefix in dic:
                    dic[prefix] = dic[prefix] + 1
        Listthing = []
        for key in dic.keys():
            if dic[key] == len(strs):
                Listthing.append(key)
        if len(Listthing) == 0:
            return ""
        return Listthing.pop() 
