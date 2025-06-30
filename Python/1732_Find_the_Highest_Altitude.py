class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        running_sum = [0]
        for i in range(len(gain)):
            running_sum.append(running_sum[i]+gain[i])
        return max(running_sum)