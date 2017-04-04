package shin.leetcode;

/**
 * Created by jiaxiaoyan on 3/30/17.

 A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

 The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

 How many possible unique paths are there?

 这里一个动态规划题，可以在这里看分析
 https://discuss.leetcode.com/topic/15265/0ms-5-lines-dp-solution-in-c-with-explanations
 很清楚。
 也就是说，如果我们在m[1][2], 那么它的步数只等于到达它上边或者左边的频数的和。
 即: m[i][j] = m[i-1][j] + m[i][j-1]
 这就是动态规划的最主要的公式

 还有两种解法，现在还没理解 。
 //TODO： 理解一下更优化的解法
 */
public class Q62_Unique_Paths {
    public int UniquePaths(int m, int n){
        if ((m == 0) || (n == 0)){
            return 0;
        }
        if ((m == 1) || (n == 1)){
            return 1;
        }
        int result[][] = new int[m][n];
        for (int i = 0; i < m; i++){
            result[i][0] = 1;
        }
        for (int j = 0; j < n; j++){
            result[0][j] = 1;
        }

        for (int i = 1; i < m; i++){
            for (int j = 1; j < n; j++){
                result[i][j] = result[i - 1][j] + result[i][j-1];
            }
        }
        return  result[m-1][n-1];

    }

    public static void main(String argv[]){
        int m = 3;
        int n = 4;
        Q62_Unique_Paths solution = new Q62_Unique_Paths();
        System.out.println(solution.UniquePaths(m,n));
    }
}
