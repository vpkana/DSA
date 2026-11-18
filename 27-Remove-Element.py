class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # n=len(nums)
        # if n==1:
        #     if val==nums[0]:
        #         return 0
        #     else:
        #         return 1
        # i=0
        # count=0
        # while i<n:
        #     if nums[i]==val:
        #         break
        #     count+=1
        #     i+=1
        # j=i+1
        # while j<n:
        #     if nums[j]!=val:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         count+=1
        #         i=i+1
        #         j=j+1
        #     else:
        #         j+=1
        # return count  
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
            
                k = k + 1
        return k

