class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                elif sum>0:
                    k=k-1
                else:
                    j=j+1
        ans=list(ans)
        return ans
                


