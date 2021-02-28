import java.util.*;
import java.util.HashMap;

public class Fence{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){

        	int n = sc.nextInt();
        	int m = sc.nextInt();
        	String ans = "";
        	int found;
        	int paintColour;
        	int leftNum = 0;

        	int[] old = new int[n];
        	int[] after = new int[n];
        	HashMap<Integer, Integer> leftOut = new HashMap<>;

        	for (int i =0; i < n; i++){
        		old[i] = sc.nextInt();
        	}

        	for (int i =0; i < n; i++){
        		after[i] = sc.nextInt();
        	}

        	for (int i =0; i < m; i++){
        		paintColour = sc.nextInt()
        		found = isIn(after,paintColour);
        		if (found == -1) {
        			if (leftOut.containsKey(paintColour) == false){
        				leftOut.put(paintColour,0);
        			}
        		}
        		else {
        			ans = ans + "" + (found +1) + " ";
        			old[found] = after[found];
        		}
        	}


        	if (leftOut.size() <= m/2) {
        		ans = "YES\n" + ans;
        		for (int i =0; i < n; i++) {
        			if (old[i] != after[i]) {
        				ans  = "NO";
        				break;
        			}
        		}
        	}
        	else {
        		ans = "N0";
        	}

        	System.out.println(ans);


        }
    }

    private static int isIn(int[] a, int num) {
    	for (int i = 0; i < a.length; i++) {
    		if (a[i] == num) {
    			return i;
    		}
    	}
    	return -1;
    }

}