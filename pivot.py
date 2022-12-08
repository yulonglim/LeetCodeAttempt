class Solution:
    def pivotIndex(self, nums):
        left = -1
        leftTot = 0
        right = len(nums)-1
        rightTot = nums[right]
        for i in range(len(nums)+1):
            if right <= left:
                return -1
            elif leftTot < rightTot:
                left += 1
                leftTot += nums[left]
            elif rightTot < leftTot:
                right -= 1
                rightTot += nums[right]
            else:
                if right - left == 2:
                    return left + 1
                else:
                    left += 1
                    leftTot += nums[left]

if __name__ == "__main__":
    Solution = Solution()
    nums = [-1,-1,-1,-1,-1,0]
    print(Solution.pivotIndex(nums))