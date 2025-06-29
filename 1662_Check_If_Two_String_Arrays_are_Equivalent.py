class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        len1 = len(word1)
        len2 = len(word2)
        string1 = ""
        index1 = 0
        string2 = ""
        index2 = 0
        for i in range(max(len1,len2)):
            if index1 != len1:
                string1+=word1[i]
                index1+=1
            if index2 != len2:
                string2+=word2[i]
                index2+=1
        return string1==string2