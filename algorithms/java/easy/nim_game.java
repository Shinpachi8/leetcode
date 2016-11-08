public class Solution {
    public boolean canWinNim(int n) {
        //case 1
        //return n % 4 != 0;
        //case 2
        return (n & 0x3) != 0;
    }
}