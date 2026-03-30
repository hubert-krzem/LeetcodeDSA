class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curCon = 0
        maxCon = 0

        i = 0
        while i < len(nums):
            if nums[i] == 1:
                curCon += 1
            else:
                if curCon > maxCon:
                    maxCon = curCon
                curCon = 0
            i += 1

        if curCon > maxCon:
            # maxCon = curCon
            return curCon
            
        return maxCon

        # Time : O(n)
        # Space: O(1)

        # Improvement:
        # Current sum = 0
        # Iterate, += 1 for each 1
        # When 0, Biggest sum = current sum
        # Current sum = 0
        # Iterate again
        # hit 0
        # If current > max, max = current
        # else
        # current = 0
        # iterate

        