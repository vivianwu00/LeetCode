class Solution(object):
    def createTargetArray(self, nums, index):
        arr = []
        for x in range(0, len(nums)):
            arr.insert(index[x], nums[x])
        return arr
        