class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi=0
        for i in accounts:
            maxii=0
            for j in i:
                maxii+=j
            if maxii>maxi:
                maxi=maxii
        return maxi