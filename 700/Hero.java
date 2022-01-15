import java.util.*;
import java.util.HashMap;

public class Hero{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){

        	int a = sc.nextInt();
        	long b = sc.nextInt();
        	int n = sc.nextInt();
        	int bi;
        	int ai;
        	int max = -1;

        	HashMap<Integer, Integer> abi = new HashMap<>();

        	for (int i =0; i < n; i++){
        		ai = sc.nextInt();
        		abi.put(i, ai);

        	}

        	for (int i =0; i < n; i++){  
        		bi = sc.nextInt();
        		b = b - head(bi, a)*abi.get(i);
        		max = Math.max(bi, max);
        	

        	}
        	if (b + max > 0){
        		System.out.println("YES");
        	}
        	else {
        		System.out.println("NO");
        	}

        }
    }

    private static int head(int a, int b) {
    	if (a%b == 0) {
    		return a/b;
    	}  

    	return a/b + 1;
    }
}