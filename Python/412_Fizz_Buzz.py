class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        endlist=[]
        if 1 <= n and n <= 10**4:
            for i in range(1,n+1):
                if i%3==0 and i%5==0 :
                    endlist.append("FizzBuzz")
                elif i%3==0:
                    endlist.append("Fizz")
                elif i%5==0:
                    endlist.append("Buzz")
                else:
                    endlist.append(str(i))
        return endlist