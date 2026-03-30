class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # First thought
        # Iterate through list
        # if i == val
        # pop (not iterating i as list will be shortened)
        # else
        # i += 1

        # Need to use while i < len, as len will change during the loop
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                # Index i removed, nums[i] = next number
            else:
                i += 1
                # Iterate to next

        return len(nums)