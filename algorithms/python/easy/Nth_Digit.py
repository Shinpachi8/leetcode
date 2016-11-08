#! /env/bin/pytho2
# coding=utf-8

"""
beat 94%
可以把str(letter) 用变量来表示 ，进一步优化
"""
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 9:
            return n
        else:
            count = 9
            letter = 10
            while  True:
                # 每次都乖2
                letter_next = letter * 2
                # 判断是否长度相同，如果长度相同，则在同一个段内，如果  100－200，这样增加的count值是
                # len(100)* (letter_next-letter) = 3 * (200-100)
                #  
                if len(str(letter_next)) > len(str(letter)):
                    # 如果长度不同， 则需要分成两部分来算。如：
                    # 80 － 160   那么要先算 80－100的count， 再算 100－160的count
                    # 80-100的count ＝ （100 － 80）* 2 ＝ (pow(10, len(str(letter))) - letter) * len(str(letter))
                    to_add1 = (pow(10, len(str(letter))) - ((letter))) * len(str(letter))

                    # 再算 100－160的count
                    # 100－160的count ＝ （160 － 100）* 3 ＝ (letter_next - pow(10, len(str(letter)))) * len(str(letter_next))
                    to_add2 = (letter_next - (pow(10, len(str(letter))))) * len(str(letter_next))
                    print len(str(count)), str(count)
                    count += to_add1


                    # 判断是否在 80－100内
                    # 如果在，那么需要算出离100有多少个数值，即 how_much = (count - n) / len(str(letter))
                    # 那么用 100 - how_much - 1 即为所在数
                    # 然后看有多少位。
                    if count >= n:
                        # print "letter: {}\t letter_next: {}\t count:{},\t to_add1:{}".format(letter,letter_next, count, to_add1)
                        # print "len(n):{}\t len(letter):{}\t len()".format(len(str(n)), len(str(letter)))
                        add = (count - n) / len(str(letter))
                        last = (count - n) % len(str(letter))
                        # print "add:{}\t last:{}\t letter+add:{}".format(add,last, letter+add)
                        # print len(str(add))
                        return ord(str(pow(10, len(str(letter))) - ((letter)) - add - 1)[len(str(letter)) - last - 1]) - 48
                    count += to_add2
                    if count >= n:
                        # print "letter: {}\t letter_next: {}\t count:{},\t to_add1:{}".format(letter,letter_next, count, to_add1)
                        # print "len(n):{}\t len(letter):{}\t len()".format(len(str(n)), len(str(letter_next)))
                        add = (count - n) / len(str(letter_next))
                        last = (count - n) % len(str(letter_next))
                        # print "add:{}\t last:{}\t letter+add:{}".format(add,last, letter_next-add)
                        # print len(str(add))
                        # print "pow(10, len(str(letter_next)):{}".format(((letter_next)) - add - 1)
                        return ord(str(letter_next - add - 1)[len(str(letter_next))-last - 1]) - 48
                    else:
                        letter = letter_next
                else:
                    to_add1 = (letter_next - letter) * len(str(letter))
                    count += to_add1
                    if count >= n:
                        add = (count - n) / len(str(letter))
                        last = (count - n) % len(str(letter))
                        return ord(str(letter_next - add - 1)[len(str(letter)) - last - 1]) - 48
                    else:
                        letter = letter_next




        # time limit
        # if n <= 9:
        #     return n
        # else:
        #     count = 9
        #     letter = 10
        #     while True:
        #         length = len(str(letter))
        #         if count + length < n:
        #             letter += 10
        #             count += length * 10
        #         elif count + length == n:
        #             return letter % 10
        #         else:
        #             print count, length,  (n-count), letter
        #             add = (n-count) / length if n-count > 0 else -(abs(n-count) / length + 1)
        #             last = (n-count) % length 
        #             print add, last-1, letter + add

        #             return ord(str(letter + add)[last-1]) - 48

        """
        # 超时
        if n <= 9:
            return n
        else:
            count = 9
            letter = 10
            while True:

                for i in str(letter):
                    count += 1
                    if count == n:
                        return ord(i) - 48
                letter += 1
        """

if __name__ == '__main__':
    n = 100000001
    print Solution().findNthDigit(n)