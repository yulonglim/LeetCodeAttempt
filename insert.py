import math
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right >= left:
            mid = math.floor((left + right) / 2)
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] > target:
                if mid == 0:
                    return 0
                if nums[mid-1] < target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                if mid == len(nums):
                    return len(nums)
                if nums[mid+1] > target:
                    return mid+1
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    Solution = Solution()
    nums = [1,3]
    print(Solution.searchInsert(nums,2))