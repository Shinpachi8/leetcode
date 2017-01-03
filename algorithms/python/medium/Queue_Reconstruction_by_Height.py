#!/usr/bin/env python
# coding=utf-8

"""
这里是我没有好好想，其实主要是按顺序来。以后想题的时候一定要好好思考
如果没头序，要先从简单的入手。
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        peo_dic, tmp, result = {}, [], []
        for p in people:
            if p[0] not in peo_dic:
                peo_dic[p[0]] = [p]
            else:
                ind = -1
                for index, value in enumerate(peo_dic[p[0]]):
                    if p[1] < value[1]:
                        ind = index
                        break
                if ind == -1:
                    peo_dic[p[0]].append(p)
                else:
                    peo_dic[p[0]].insert(ind, p)

        tmp = sorted(peo_dic, reverse=True)
        print peo_dic
        for height in tmp:
            # peos = self.sort_list(peo_dic[height])
            for k in peo_dic[height]:
                result.insert(k[1], k)
                # print result

        return result

    def sort_list(self, li):
        lens = len(li)
        index = 0
        while index < lens - 1:
            mins = index
            for tmp in range(index + 1, lens):
                if li[mins][1] > li[tmp][1]:
                    # print "li[{}][1]:{}, li[{}][1]:{}".format(index, li[index][1], tmp, li[tmp][1])
                    mins = tmp
            # print "mins:{}\tindex:{}".format(mins,index)
            if mins != index:
                li[index], li[mins] = li[mins], li[index]
            index += 1
        return li

if __name__ == '__main__':
    people = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]
    b = Solution().reconstructQueue(people)
    print b



