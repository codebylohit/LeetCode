class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for i in jewels:
            if i in stones:
                sum+=stones.count(i)
        return sum