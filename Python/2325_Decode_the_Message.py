class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        x=97
        final=""
        hashm={" ":" "}
        seen=set()
        for i in key:
            if i not in seen and i != " ":
                hashm[i]=chr(x)
                x+=1
                seen.add(i)
        for i in message:
            final+=hashm[i]
        return final