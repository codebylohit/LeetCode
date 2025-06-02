class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #first try
        '''for i in nums:
            if nums.count(i)==1:
                return i'''
        
        #optimised solution
        result = 0
        for num in nums:
            result ^= num
        return result
