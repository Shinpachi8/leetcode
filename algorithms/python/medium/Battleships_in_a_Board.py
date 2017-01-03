#! /usr/bin/env python3
# coding=itf-8

"""
@version: 1.0
参考别人代码:  对与每一行战舰, 如果这个点是x, 那么我们只需要去看他的上一层与左一层是否是x, 
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != "X":
                    continue
                if i > 0 and board[i-1][j] == "X":
                    continue
                if j > 0 and board[i][j-1] == "X":
                    continue
                result += 1
                
        

        return result