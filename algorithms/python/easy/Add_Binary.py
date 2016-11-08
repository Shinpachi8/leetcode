#! /usr/bin/env python3
# coding=utf-8

"""
beat 94%
可以优化: 
    1. 设置一个 长度为 max(len(a), len(b)) ＋ 1 的列表
    将列表的值初置为-1 , 由后向前添
    2. 设置一个stack, 依次向里添加， 最后取出
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        # 看是a/b 哪一个长度比较长， 如果b比较长，那么将a,b互换
        if length_a < length_b:
            a, b = b, a
            length_a, length_b = length_b, length_a

        # 看 a/b的长度差是多少
        diff = length_a - length_b

        # 将a分为与b长度相同的一部分，与比b长的那一部分,
        # low_a 与 b做 加法运算
        # high_a 自己做运算
        low_a = a[diff:]
        high_a = a[0: diff]

        # 设置进位标志, 与结果
        carry = 0
        result = ""

        # 将序列反过来做运算
        for i in range(length_b - 1, -1, -1):
            # ord(x) - 48 即是将str 转 int
            add_value = ord(low_a[i]) - 48 + ord(b[i]) - 48
            # 如果进位
            if carry != 0:
                add_value += carry
                carry = 0
            # 判断进位是几
            carry = add_value / 2
            result += str(add_value % 2)

        # 将多的那一部分做运算
        for i in range(diff - 1, -1, -1):
            # 先判断是否有下一位进来的进位
            if carry != 0:
                add_value = ord(high_a[i]) - 48 + carry
                carry = 0
                carry = add_value / 2
                result += str(add_value % 2)
            else:
                result += high_a[i]
        # 最后判断是否有进位
        if carry:
            result += "1"

        # 将结果向逆即可得最终结果
        temp = ""
        for i in range(len(result), 0, -1):
            temp += result[i - 1]
        return temp


if __name__ == '__main__':
    a = "100"
    b = "1"
    print Solution().addBinary(a, b)
