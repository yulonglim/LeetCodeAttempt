class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while right >= left:
            mid = math.floor((left + right) / 2)
            if isBadVersion(left):
                return left
            if isBadVersion(right):
                return right
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                right = mid - 1
            else:
                if isBadVersion(mid+1):
                    return mid+1
                left = mid + 1
        return -1