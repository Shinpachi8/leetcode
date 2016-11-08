#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://leetcode.com/problems/compare-version-numbers/


"""
看了一下其他几个人的想法， 尤其是0ms的C++/JAVA的解法
1. 不转换成整数，而是在分隔.之后的字符串中对比， 先求出每个.分隔之后的字符串，然后求出长度的相差
    最后在短的那个字符串前加入00， 比齐之后再比较字符串

2. 思想同1， 但是在分割出.隔开的string之后， 将首0去掉，再比较长度， 如果长度相同，再比较具体的内容。



"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # if max(version1.count('.'), version2.count('.')) < 2:
        #     fversion1 = float(version1)
        #     fversion2 = float(version2)
        #     if fversion1 > fversion2:
        #         return 1
        #     elif fversion1 == fversion2:
        #         return 0
        #     else:
        #         return -1
        
        
        aa = [int(x) for x in version1.split('.')]
        bb = [int(x) for x in version2.split('.')]
        
        aa_length = len(aa)
        bb_length = len(bb)
        min_length = min(aa_length, bb_length)

        for i in range(0, min_length):
            if aa[i] == bb[i]:
                continue
            if aa[i] > bb[i]:
                return 1
            if aa[i] < bb[i]:
                return -1
        
        # for i, j in zip(aa, bb):
        #     if i == j:
        #         continue
        #     if i > j:
        #         return 1
        #     if i < j:
        #         return -1
        
        if aa_length == bb_length:
            return 0
        
        if aa_length == min_length:
            for i in range(min_length, bb_length):
                if bb[i] > 0:
                    return -1
            return 0

        for i in range(min_length, aa_length):
            if aa[i] > 0:
                return 1
        return 0
        
            
        # aaf = aa[min_length:]
        # bbf = bb[min_length:]
        
        
        
        # if len(aaf) == 0 and len(bbf) == 0:
        #     return 0
        # if len(aaf) == 0 and len(bbf) > 0:
        #     for i in bbf:
        #         if i > 0:
        #             return -1
        #     return 0
        # if len(bbf) == 0 and len(aaf) > 0:
        #     for i in aaf:
        #         if i > 0:
        #             return 1
        #     return 0
            
            