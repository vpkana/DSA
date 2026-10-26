class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        def helper(l,r,t):
            if l>n or r>n or l<r:
                return 
            if l==r and l==n:
                return result.append(t)
            helper(l+1,r,t+'(')
            helper(l,r+1,t+')')
        helper(0,0,'')
        return result