class Solution(object):
    def decompressRLElist(self, nums):
        arr = []
        for x in range(0, len(nums) - 1):
            if x%2 == 0:
                for y in range(nums[x]):
                    arr.append(nums[x+1])
        return arr

        
        