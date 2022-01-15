import java.util.*;

public class q1{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	int a = sc.nextInt();
        	int b = sc.nextInt();

        	System.out.println(kdoRec(a,b,0));
        	
        }
    }

    private static int kdoRec(int a, int b, int k) {

        // System.out.println(a + " " + b);

    	if (a == 0) {
    		return k;
    	} 

    	else if (a/b == 0) {
    		a = a/b;
    	}
        else if (a/(b+1) == a/b) {
            a = a/b;
        }
    	else {
    		b +=1;
    	}
        k += 1;
        return kdoRec(a,b,k);
    }

}