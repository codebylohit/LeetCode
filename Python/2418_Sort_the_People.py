class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = len(names)
        mapped={}
        for ind in range(n):
            mapped[heights[ind]] = names[ind]
        heights.sort(reverse = True)
        for ind in range(n):
            h = heights[ind]
            names[ind] = mapped[h]

        return names