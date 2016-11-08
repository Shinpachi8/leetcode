#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        total = len(ransomNote)
        len_of_magazine = len(magazine)
        i = 0
        j = 0
        print total,len_of_magazine
        if total == 0 and len_of_magazine > 0:
            return True
        if total > 0 and len_of_magazine == 0:
            return False
        dict_ransom = {}
        dict_magazine = {}
        for i in ransomNote:
            if i in dict_ransom:
                dict_ransom[i] += 1
            else:
                dict_ransom[i] = 1
        for j in magazine:
            if j in dict_magazine:
                dict_magazine[j] += 1
            else:
                dict_magazine[j] = 1

        for i in dict_ransom:
            if i not in dict_magazine or dict_magazine[i] < dict_ransom[i]:
                return False

        return True

if __name__ == '__main__':
    s = "bjaajgea"
    m = "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"
    if (Solution().canConstruct(s,m)):
        print "True"
    else:
        print "False"