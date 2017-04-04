import javax.xml.stream.FactoryConfigurationError;

/**
 * Created by jiaxiaoyan on 3/28/17.
 */
public class Q74_Search_a_2D_Matrix {
    public static void main(String argv[]){
        int target = 3;
        int[][] matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,50}};

        Q74_Search_a_2D_Matrix test = new Q74_Search_a_2D_Matrix();
        boolean result = test.searchMatrix(matrix, target);
        if (result){
            System.out.print("Find");
        }else{
            System.out.print("Not Find");
        }
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        int m = 0, n = 0, i_row = 0;
        m = matrix.length;
        if (m == 0){
            return false;
        }else{
            n = matrix[0].length;
            if (n == 0){
                return false;
            }
        }
        for (int i=0; i < m; i++){
            if (matrix[i][n-1] >= target){
                i_row = i;
                break;
            }
        }

        int low = 0, high = n-1, mideum = (low + high) / 2;
        while (low <= high){
            if (matrix[i_row][mideum] == target){
                return true;
            }else if (matrix[i_row][mideum] < target){
                low = mideum + 1;
                mideum = (low + high) / 2;
            }else{
                high = mideum - 1;
                mideum = (low + high) / 2;
            }
        }
        return false;

    }
}
