import java.util.*;

public class Segment2{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	int[] arr = new int[n];

    	for (int i =0; i < n; i++){
    		arr[i] = sc.nextInt();
    	}

    	System.out.println(seg(arr));
    }


    private static int seg(int[] arr) {
    	int prevB = -1;
    	int prevW;
    	int ans = 1;
    	boolean isWhite = true;
    	int n = arr.length;

    	if (n <= 1) {
    		return n;
    	}

    	else {
    		prevW = arr[0];
    		for (int i = 1; i <n ; i++) {
                if (isWhite) {
    				if (arr[i] != prevW) {
    					isWhite = false;
    					if (prevB != arr[i]) {
    						ans += 1;
    						prevB = arr[i];
    					}
    				}
    			}

    			else{
    				if (arr[i] != prevB) {
    					isWhite = true;
    					if (prevW != arr[i]) {
    						ans += 1;
    						prevW = arr[i];
    					}
    				}
    			}
    		}
    	}

    	return ans;
    	

    }
}