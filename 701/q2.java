import java.util.*;

public class q2{


	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int q = sc.nextInt();
        int k = sc.nextInt();
        int l;
        int r;
        double ans;

        int[] array = new int[n];

        for (int i = 0; i<n; i++) {
        	array[i] = sc.nextInt();
        }

        for (int i = 0; i<q; i++) {
        	l = sc.nextInt() -1;
        	r = sc.nextInt()-1;
        	System.out.println(array[l+1]);
        	ans = Math.pow(2,r-l-1)*(array[l+1] -1)*(k-array[r-1]-1);
        	System.out.println((int)ans);
        }

    }


}