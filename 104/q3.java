import java.util.*;
// import java.util.HashMap;

public class q3{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	long n = sc.nextInt();
        	System.out.println(countSquares((2*n)-1));
        }
    }

    private static int countSquares(long b) 
    { 
        return (int)Math.ceil(Math.floor(Math.sqrt(b))/2) - 1;
    } 
}