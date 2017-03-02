#! /usr/bin/env python3
# coding+utf-8

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_h = len(haystack)
        length_n = len(needle)
        if length_n > length_h:
            return -1

        if needle == haystack:
            return 0

        flag = 1
        for i in range(length_h - length_n + 1):
            for j in range(length_n):
                print ("i:{}, j:{}\n "
                    "haystack[i+j]:{},needle[j]:{}").format(i,j,haystack[i+j], needle[j])
                if haystack[i+j] != needle[j]:
                    flag = 0
                    break
            if flag == 1 :
                return i
            else: 
                flag = 1

        return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle =  "pi"
    print Solution().strStr(haystack, needle)

