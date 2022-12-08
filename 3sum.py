class Solution:
    def threeSum(self, nums):
        output = []
        nums.sort()
        for i in range(len(nums)):
            subset = self.twoSum(nums[i+1:], -nums[i])
            for sol in subset:
                sol.append(nums[i])
                if sol not in output:
                    output.append(sol)
        return output

    def twoSum(self,nums,target):
        dic= {}
        for i in nums:
            if target-i not in dic:
                if i not in dic:
                    dic[i] = []
            else:
                dic[target-i].append(i)
        
        output = []
        for i in dic.keys():
            if len(dic[i]) > 0:
                for j in dic[i]:
                    output.append([i,j])
        return output

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    Solution = Solution()
    print(Solution.threeSum(nums))