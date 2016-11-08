#! /usr/bin/env python
# -*- coding:utf-8 -*-

#https://leetcode.com/problems/zigzag-conversion/


"""
前5%的解法，可以看出，他没有用 +、-2，而是每次都加2*numRow-2 这个间距，并把
它之前的 相差2*i的数加上， 这样确实比较快
还不用写其他的函数


public String convert(String s, int numRows) {
    if(numRows==1) return s;
    int x = 2 * (numRows-1); // distance between pipes |/|/|...
    int len = s.length();
    char[] c = new char[len];
    int k =0;
    for(int i=0; i < numRows; i++)
    {
        for(int j=i;j<len;j=j+x)
        {
            c[k++] = s.charAt(j);
            if(i>0 && i<numRows-1 && j+x-2*i < len)
            {
                   c[k++] = s.charAt(j+x-2*i); // extra character between pipes
            }
        }
    }
    return new String(c);
}

"""
import pdb


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= numRows:
            return s
        if numRows == 1:
            return s

        ans = ""
        # pdb.set_trace()
        magic = 2 * numRows - 2
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                print i, 'times'
                ans += self.file(i, 0, magic, s)
            else:
                print i, 'times'
                ans += self.file(i, 2 * i, magic, s)
        return ans

    def file(self, start, initDistance, magic, s):
        ans = ""
        index = start
        length = len(s)
        while(index < length):
            ans += s[index]
            print ans
            if initDistance == 0:
                index = index + magic
            else:
                index = index + magic - initDistance
                initDistance = magic - initDistance
        return ans

if __name__ == '__main__':
    a = Solution()
    b = 'ABCDE'
    print a.convert(b, 4)
