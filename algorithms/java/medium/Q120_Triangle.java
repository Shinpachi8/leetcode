package shin.leetcode;
import org.jetbrains.annotations.NotNull;

import java.util.List;
import java.util.ArrayList;
/**
 * Created by jiaxiaoyan on 3/31/17.
 * https://leetcode.com/problems/triangle/#/description
 * dp
 */
public class Q120_Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        int col = triangle.size();
        if (col == 0){
            return triangle.get(0).get(0);
        }
        int result[][] = new int[col][col];
        for (int i = 0; i < col; i++){
            for (int j = 0; j <= i; j++){
                if (i == 0){
                    result[i][j] = triangle.get(0).get(0);
                }
                if ((j == 0) || (j == i)){
                    result[i][j] = result[i - 1][j] + triangle.get(i).get(j);
                }else{
                    result[i][j] = Math.min(result[i-1][j], result[i-1][j-1]) + triangle.get(i).get(j);
                }
            }
        }
        int re = result[col-1][0];
        for (int i : result[col - 1]){
            if (i < re){
                re = i;
            }
        }
        return re;
    }

    public static void main(String[] args){
        List<List<Integer>> li = new ArrayList<List<Integer>>();
        List<Integer> tmp = new ArrayList<Integer>();
        tmp.add(0);
        li.add(tmp);
        for (List<Integer> a : li){
            for (int i : a){
                System.out.println(i);
            }
        }

    }
}
