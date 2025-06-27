class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        output=[]
        index=0
        for i in words:
            if x in i:
                output.append(index)
            index+=1
        return output