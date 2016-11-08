#! /usr/bin/env python
# -*- coding:utf-8 -*- 

#https://leetcode.com/problems/reverse-vowels-of-a-string/

"""
这个题本来是挺简单的，但是我想复杂了
题意是将元音字母反转， 只要两个指针从头和尾相遇就可以了
但是我想的是 只有发音的两个字母....
而且我以为最后一个字母是不换的.... ORZ

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return s
        
        vowels = ['a', 'e', 'i', 'o', 'u'] 
        temp = list(s)
        start = 0
        end = len(s)-1

        while(start < end):
            if s[start].lower() not in vowels:
                start += 1
            elif s[end].lower() not in vowels:
                end -= 1
            else:
                temp[start], temp[end] = temp[end], temp[start]
        return "".join(temp)
#        while(start < end):
#
#            if s[start].lower() in vowels and s[end].lower() in vowels:
#                value = temp[start]
#                temp[start] = temp[end]
#                temp[end] = value
#                start += 1
#                end -= 1
#            elif s[start].lower() in vowels and s[end].lower()not in vowels:
#                end -= 1
#            elif s[end].lower() in vowels and s[start].lower() not in vowels:
#                start += 1
#            else:
#                start += 1
#                end -= 1
#        
#        ans = ''
#        return ans.join(temp)
#        # for i in temp:
        # ans += i 
        # return ans


if __name__ == '__main__':
    print Solution().reverseVowels("hello")
