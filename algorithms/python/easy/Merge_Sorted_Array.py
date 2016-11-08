#! /env/bin/python2
# coding=utf-8

"""
beat 92%

"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0 and m != 0:
            pass
        else:
            temp = nums1[0:m]
            i, j, k = 0, 0, 0

            while(i < m or j < n):
                if i < m and j < n:
                    if temp[i] < nums2[j]:
                        nums1[k] = temp[i]
                        k += 1
                        i += 1
                    else:
                        nums1[k] = nums2[j]
                        k += 1
                        j += 1
                elif i < m:
                    nums1[k] = temp[i]
                    k += 1
                    i += 1
                elif j < n:
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1


"""
beat 73%
            # mark =  0
    
            # for i in range(n):
            #     if nums1[m + i - 1] <= nums2[i]:
            #         for k in range(i, n):
            #             nums1[m + k] = nums2[k]
            #     else:
            #         for j in range(mark, m+n):
            #             if nums2[i] <= nums1[j]:
            #                 mark = j
            #                 temp = m + i
            #                 print "i is: {}\tj is: {}\tmark is:  {}\ttemp is: {}".format(i, j, mark, temp)
            #                 while(temp > j):
            #                     nums1[temp] =nums1[temp - 1]
            #                     temp -= 1
            #                 nums1[j] = nums2[i]
            #                 break

        return nums1

"""
if __name__ == '__main__':
    nums1 = [2,0]
    nums2 = [1]
    m = 1
    n = 1
    print Solution().merge(nums1, m, nums2, n)




