# 440. K-th Smallest in Lexicographical Order

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result + 1]
            while interval[0] <= n:
                count += min(n + 1, interval[1]) - interval[0]
                interval = [interval[0] * 10, interval[1] * 10]

            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1

        return result


a = Solution()

print a.findKthNumber(2, 2)
