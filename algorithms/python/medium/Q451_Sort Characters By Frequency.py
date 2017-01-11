#!/usr/bin/env python
# coding=utf-8

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        mins, maxs = ord(min(s)), ord(max(s))
        print maxs, mins
        tmp_li = [0] * (maxs - mins + 1)
        tmp_dic = {}
        result = ""
        for i in s:
            tmp_li[ord(i) - mins] += 1
        for index, value in enumerate(tmp_li):
            if value == 0:
                continue
            else:
                if value in tmp_dic:
                    tmp_dic[value] += chr(index + mins)
                else:
                    tmp_dic[value] = chr(index + mins)

        for i in sorted(tmp_dic, reverse=True):
            if len(tmp_dic[i]) > 1:
                for j in tmp_dic[i]:
                    result += j * i
            else:
                result += tmp_dic[i] * i
        return result


if __name__ == '__main__':
    s = "Aabb"
    print Solution().frequencySort(s)
