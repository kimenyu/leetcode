class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x)):
            for j in range(len(x))[::-1]:
                return x[i] == x[j]