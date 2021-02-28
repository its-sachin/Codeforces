import java.util.*;

public class q3{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	int a = sc.nextInt();
        	int b = sc.nextInt();
        	int ans = 0;
        	int al = a;
        	int bl = b;

        	while (al != 0) {
        		while (b != 0) {
        			if (a%b == a/b){
        				ans += 1;
        			}
        			b -=1;
        		}
        		bl = b;
        		al -=1;
        	}

        	System.out.println(ans);
        }
    }

}