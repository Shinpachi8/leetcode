#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def Isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == "" and t == "":
            return True
        if s and not t:
            return False
        if t and not s:
            return False

        dict_s = {}
        dict_t = {}
        dict_s_2_t = {}

        length = len(s)
        for i in range(length):
 
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 0

            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 0

            if s[i] in dict_s_2_t:
                if not dict_s_2_t[s[i]] == t[i]:
                    return False
            else:
                dict_s_2_t[s[i]] = t[i]


        for i in s:

            if not dict_s[i] == dict_t[dict_s_2_t[i]]:
                return False
        return True


if __name__ == '__main__':
    s = "foo"
    t = "bar"
    if Solution().Isomorphic(s, t):
        print "True"
    else:
        print "False"


