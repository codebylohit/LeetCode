class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        final = []

        for word in words:
            wordd = set(word.lower())
            if wordd.issubset(row1) or wordd.issubset(row2) or wordd.issubset(row3):
                final.append(word)
                
        return final