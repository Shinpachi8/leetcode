public class Solution {
    public int getSum(int a, int b) {
        //这里用的是反码与补码与原码的概念
        // 原码： 1： 0001 ， -1：1001；  
        // 反码： 1:  0001,   -1: 1110；  正数不变，负数除最高位后其他取反
        // 补码： 1： 0001，  -1：1111；  正数不变， 负数在反码的基础上加1
        int temp;
        while(b!=0){
            temp = a ^ b;
            b = (a & b) << 1;
            a = temp;
        }
        return a;
    
    }

}