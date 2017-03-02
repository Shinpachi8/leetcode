#! /usr/bin/env python3
# coding=utf-8

"""
beat: 89%
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        strs_len = len(strs)
        if strs_len == 0:
            return common
        if strs_len == 1:
            common = strs[0]
            return common

        min_length = len(strs[0])
        for i in strs:
            ss = len(i)
            if ss < min_length:
                min_length = ss

        
        for i in range(min_length):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    return common
            common += temp
        return common


if __name__ == '__main__':
    strs = ["aca","cba"]
    print Solution().longestCommonPrefix(strs)
