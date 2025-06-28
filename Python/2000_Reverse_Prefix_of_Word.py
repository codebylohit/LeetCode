class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = 0
        store_index = 0
        for letter in word:
            if letter == ch:
                store_index=index
                break
            index+=1
        return (word[:store_index+1][::-1] + word[store_index+1:])