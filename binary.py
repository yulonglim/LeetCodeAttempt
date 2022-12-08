import math
class Solution:
    def search(self, nums, target: int):
        left = 0
        right = len(nums)-1
        while right >= left:
            mid = math.floor((left + right) / 2)
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    Solution = Solution()
    nums = [-1,0,3,5,9,12]
    print(Solution.search(nums,2))