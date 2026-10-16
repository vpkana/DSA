class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        rev=0
        rem=0
        temp=x
        while temp is not 0:
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
        if rev==x:
            return True
        else:
            return False