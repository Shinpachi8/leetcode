#! /env/bin/python2
# coding=utf-8


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_list = [0] * 10
        guess_list = [0] * 10
        bull = 0
        cows = 0

        length = len(secret)
        for i in range(length):
            if guess[i] == secret[i]:
                bull += 1
            else:
                secret_list[int(secret[i])] += 1
                guess_list[int(guess[i])] += 1
            print "bull is {}, secret_list is {} \n \t\t   guess_list is  {}".format(bull, secret_list, guess_list)
        for i in range(10):
            cows += min(secret_list[i], guess_list[i])

        return str(bull)+"A"+str(cows)+"B"


if __name__ == '__main__':
    secret = "1123"
    guess = "0111"
    print Solution().getHint(secret, guess)

