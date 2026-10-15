class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum=0
        for i in range(0,len(nums)):
            mset=set()
            for j in range(i,len(nums)):
                mset.add(nums[j])
                l=len(mset)
                sum+=l*l
        return sum
