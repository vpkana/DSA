class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        nums.sort()
        sum=0
        count=0
        odd=len(nums)//2
        for i in nums:
            if count<odd:
                sum=sum-i
                count+=1
            else:
                sum=sum+i
        return sum
        