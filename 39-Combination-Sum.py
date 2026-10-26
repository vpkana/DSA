class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        def helper(index, total, curr):
            if total>target or index==len(candidates):
                return
            if total==target:
                return result.append(curr)
            helper(index,total+candidates[index],curr+[candidates[index]])
            val=index+1
            if val<len(candidates):
                helper(index+1,total,curr)

        helper(0,0,[])
        return result