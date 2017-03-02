#! /usr/bin/env python3
# coding=utf-8


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        extral = {}
        count = 0
        for i in board:
            if i in extral:
                pass
            else:
                extral[i] = 0

        return len(extral)


if __name__ == '__main__':
    board = ["X..X","...X","...X"]
    print Solution().countBattleships(board)

