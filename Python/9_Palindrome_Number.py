class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        '''if x <= (2**31 - 1) or -2**31 <= x:
            if list(str(x))==list(str(x))[::-1]:
                return True
            else:
                return False
        else:
            return False'''
        
        #optimised one below

        if x<0:
            return False
        reverse=0
        xdupe=x
        while x>0:
            reverse=reverse*10+(x%10)
            x//=10

        return reverse==xdupe