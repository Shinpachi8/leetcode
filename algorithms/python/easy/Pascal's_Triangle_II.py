#! /env/bin/pythoh2
# coding= utf-8


"""
1. 首先生成一个数组，长度为结果的长度
2. 再依次做循环将数值插入进去。
具体来说
    从第2位开始添加，
    第二位等于上一次的结果的第一位和第二位的和

    这里还有PYTHON的一个深浅拷贝的问题。
    必须重新生成一个数组，或者用深拷贝，不能直接复制

"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        if rowIndex == 2:
            return [1, 1]

        result = [0] * (rowIndex + 1)
        result[0] = 1
        result[1] = 1
        result[rowIndex] = 1
        temp = result

        for i in range(2, rowIndex + 1):
            # print "temp:{}\n result:{}".format(temp, result)
            print i
            for j in range(1, i):
                # print "temp:{}\n result:{}".format(temp, result)

                value = temp[j - 1] + temp[j]
                print "value is {} \t result[{}] is {}".format(value, j, value)
                result[j] = value
            result[i] = 1
            temp = []
            # 深浅拷贝
            for i in result:
                temp.append(i)
            print temp

        return result


if __name__ == '__main__':
    rowIndex = 5
    print Solution().getRow(rowIndex)
