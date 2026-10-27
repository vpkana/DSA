class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result=[]
        def helper(index,total,val,curr):
            if index==k:
                if total==n:
                    return result.append(curr)
                return
            if total>n:
                return
            if val>9:
                return
            helper(index+1,total+val,val+1,curr+[val])
            helper(index,total,val+1,curr)
            
        helper(0,0,1,[])
        return result