class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newarray = nums1+nums2
        newarray.sort()
        if(len(newarray)%2 == 1):
            return newarray[(len(newarray)-1)//2]
        midian = newarray[(len(newarray)-1)//2] +newarray[((len(newarray)-1)//2)+1]
        
        return midian/2
        