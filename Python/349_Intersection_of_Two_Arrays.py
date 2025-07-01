class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        repeater=set()
        nums2copy=set(nums2)
        for i in nums1:
            if i in nums2copy:
                repeater.add(i)
        return list(repeater)
