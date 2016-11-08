#! /env/bin/python2
# coding=utf-8

class Solution(object):
    """docstring for Solution"""
    def fizzBuzz(self,n):
        """
        :type n:int
        :rtype :  List[str]
        """

        if n <= 0:
            return

        i = 1
        result = []
        while(i <= n):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
                i += 1
                continue

            if i % 3 == 0:
                result.append("Fizz")
                i += 1
                continue

            if i % 5 == 0:
                result.append("Buzz")
                i += 1
                continue

            result.append(str(i))
            i += 1
        return result


if __name__ == '__main__':
    a = Solution().fizzBuzz(15)
    print a
