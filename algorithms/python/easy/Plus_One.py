class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        jinwei = 0
        length = len(digits)
        while (length > 0):
            temp = digits[length-1] + 1
            if temp >= 10:
                jinwei = 1
                digits[length-1] = temp%10
            else:
                digits[length-1] = temp
            if not jinwei:
                return digits
            else:
                length = length -1
                jinwei = 0
        print len(digits)
        if digits[0] == 0:
            result = [1]
            for i in digits:
                result.append(i)
            
            print  result
            return result
        else:
            return digits


if __name__ == '__main__':
    digits = [2,4,9,3,9]
    print Solution().plusOne(digits)