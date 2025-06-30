class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=sorted((nums))
        dictt={}
        for i, num in enumerate(temp):
            if num not in dictt:
                dictt[num]=i
        ret=[]
        for i in nums:
            ret.append(dictt[i])

        return ret