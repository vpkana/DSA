class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        def storeSubset(bucket,index):
            if index == len(nums):
                return result.append(bucket)

            storeSubset(bucket + [nums[index]], index+1)
            storeSubset(bucket,index+1)

        storeSubset([],0)
        return result
