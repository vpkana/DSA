class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        candidates.sort()
        def helper(total,index,curr):
            if total==target:
                return result.append(curr)
            if total>target or index==len(candidates):
                return
            helper(total+candidates[index],index+1,curr+[candidates[index]])
            next=index+1
            while next<len(candidates):
                if candidates[index]!=candidates[next]:
                    break
                next+=1
            helper(total,next,curr)
            
        helper(0,0,[])
        return result