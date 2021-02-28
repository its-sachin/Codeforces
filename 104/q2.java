import java.util.*;
// import java.util.HashMap;

public class q2{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	long n = sc.nextInt();
        	long k = sc.nextInt();
        	System.out.println(cat(n,k));


        }
    }

    private static long cat(long n, long k){
    	long b = 1;

    	while (k-- > 1){
    		b = b+2;
    		if ( b >= n+1) {
    			b = b%n;
    		}

    		if (b == n) {
    			b = b + 1;
    			if (b== n+1) {
	    			b = 1;
	    		}
    		}
    		// System.out.println(n + " " +b);
    	}

    	long a = n;
    	if (k > n) {
    		while (k>n) {
    			k = k - n;
    		}
    		if ( k != n) {
    			a = a - k;
    		}
    	}


    	return (a+b);
    }
}