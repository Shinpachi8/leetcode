#! /env/bin/python2
# coding=utf-8

"""
beat 93%
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list_str = str.split(" ")
        length_pattern = len(pattern)
        legnth_str = len(list_str)

        dict_pattern = {}
        if legnth_str != length_pattern:
            return False

        for i in range(legnth_str):
            if pattern[i] in dict_pattern:
                if list_str[i] != dict_pattern[pattern[i]]:
                    return False
            else:
                if dict_pattern:
                    for j in dict_pattern:
                        if dict_pattern[j] == list_str[i]:
                            return False

                    dict_pattern[pattern[i]] = list_str[i]
                else:
                    dict_pattern[pattern[i]] = list_str[i]

        return True


if __name__ == '__main__':
    pattern = "aaaa"
    str = "dog cat cat dog"
    if Solution().wordPattern(pattern, str):
        print  "yes"
    else:
        print "no"