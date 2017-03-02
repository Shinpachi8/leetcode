#! /usr/bin/env python3
# coding=utf-8

"""
用python时不需要考虑int类型的大小，但是用其他的强类型的语言时，一定要考虑

"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0
        result = 0
        has_sinbol = False
        char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        passtive = True
        for value in str:
            if has_sinbol:
                if value in char_list:
                    result = result * 10 + (ord(value) - 48)
                else:
                    if passtive:
                        result = result if result <= 2147483647 else 2147483647
                    else:
                        result = -result if -result >= -2147483648 else -2147483648
                    return result
            else:
                if value == " ":
                    continue
                elif value in char_list:
                    has_sinbol = True
                    result = result * 10 + (ord(value) - 48)
                else:
                    if value == "+":
                        has_sinbol = True
                        passtive = True
                    elif value == "-":
                        has_sinbol = True
                        passtive = False
                    else:
                        return 0

        if passtive:
            result = result if result <= 2147483647 else 2147483647
        else:
            result = -result if -result >= -2147483648 else -2147483648
        return result


if __name__ == '__main__':
    str = "2147483648"
    print Solution().myAtoi(str)