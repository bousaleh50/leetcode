class Solution:
    """
     if the array is sorted it's easy to think of using the binary search algorithm
     so here is the answer using binary search algorithm
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        low =  0
        heigh = len(nums)-1
        while(low<=heigh):
            mid = low +(heigh-low)//2
            if(nums[mid]== target):
                return mid
            if(target > nums[mid]):
                low = mid+1
            else:
                heigh=mid-1
        return low