package shin.leetcode;
import java.util.ArrayList;
import java.util.List;
/**
 * Created by jiaxiaoyan on 4/4/17.
 * 同样是两种方法，一种是用迭代
 * 另外一种是用比特位，参见python
 * 还有一种方法是递归，但是这个还没理解 。
 * 后继再说吧
 */
public class Q78_Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        // 用迭代
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        // 初始值置空
        result.add(new ArrayList<Integer>());

        for(int num : nums){
           int size = result.size();
           for (int j = 0; j < size; ++j){
               List<Integer> tmp = new ArrayList<>(result.get(j));
               tmp.add(num);
               result.add(tmp);
           }

        }
        return result;


    }

    public  static  void main(String[] args){
        int[] nums = {1,2,3};
        Q78_Subsets q78 = new Q78_Subsets();
        List<List<Integer>> result = q78.subsets(nums);
        System.out.println(result);
    }
}
