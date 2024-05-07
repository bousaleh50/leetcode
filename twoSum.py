class Solution:
    "This code ru"
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            if(target-nums[i] in indices):
                return [i,indices[target-nums[i]]]
            indices[nums[i]] = i
    


