class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum1=0
        xcopy=x
        while x>0:
            sum1+=x%10
            x=x//10
        if xcopy%sum1==0:
            return sum1
        return -1