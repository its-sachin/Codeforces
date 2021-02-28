import java.util.*;
// import java.util.HashMap;

public class q1{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	int n = sc.nextInt();
        	int[] ai = new int[n];      	

        	for (int i = 0; i<n; i++) {
        		ai[i] = sc.nextInt();
        	}

        	System.out.println(n-minCount(ai));	
        }
        
    }

    private static int minCount(int[] array) {

    	int min = 101;

    	for(int i=0; i<array.length; i++) {
    		min = Math.min(array[i], min);
    	}

    	int out = 0;

    	for(int i=0; i<array.length; i++) {
    		if (array[i] == min) {
    			out += 1;
    		}
    	}

    	return out;

    }
}	