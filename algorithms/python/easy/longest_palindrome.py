#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict_a = {}
        for i in s:
            if i in dict_a:
                dict_a[i] += 1
            else:
                dict_a[i] = 1
        length = 0
        max_a = 0
        if len(dict_a) == 1:
            return dict_a[s[0]]
        for i in dict_a:
            if dict_a[i] % 2 == 0:
                length += dict_a[i]
            else:
                if max_a < dict_a[i]:
                    max_a = dict_a[i]
                length += dict_a[i] / 2 * 2
        
        
        return max_a + length - max_a /2 * 2
            





if __name__ == '__main__':
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print "length of s is {}".format(len(s))
    print Solution().longestPalindrome(s)