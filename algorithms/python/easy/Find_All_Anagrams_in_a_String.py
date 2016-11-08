#! /env/bin/python2
# coding=utf-8

#https://discuss.leetcode.com/topic/65032/python-o-n-time-o-1-space
# 对于每个值，根据他的ascii码值来做一个哈希表，
# 再长度一定的时候只操作数值就行。
# 比字典要快的多。

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        length_s = len(s)
        length_p = len(p)
        if length_s < length_p:
            return []

        result = []
        phash = [0]*123
        shash = [0]*123


        for i in p:
            phash[ord(i)] += 1

        for i in s[0:(length_p-1)]:
            shash[ord(i)] += 1


        for i in range(length_p-1, length_s):
            print i,
            shash[ord(s[i])] += 1
            if i >= length_p:
                shash[ord(s[i - length_p])] -= 1
            if shash == phash:
                result.append(i - length_p + 1)

        return result


if __name__ == '__main__':
    s = "abab"
    p = "ab"
    print Solution().findAnagrams(s, p)
