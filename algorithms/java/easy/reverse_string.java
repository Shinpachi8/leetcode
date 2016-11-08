//https://leetcode.com/problems/reverse-string/
public class Solution {
    public static String reverseString(String s) {
        
        if (s.length() == 0 || s.length() == 1){
            return s;
        }
        int length = s.length();
        char[] ans = new char[length];
        
        for( int i= length-1, j=0; i>=0; i--,j++){
            ans[j] = s.charAt(i);
        }
        return new String(ans);
    }

    public static void main(String[] args) {
        String s = "hello";
        System.out.println(reverseString(s));
    }
}