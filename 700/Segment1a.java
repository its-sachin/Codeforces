import java.util.*;

public class Segment1a{

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
        int n = arr.length;
        if (n <= 1) {
            return n;
        }   	 

        else {
            int[] seg1 = new int[n];
            int[] seg2 = new int[n];
            seg1[0] = arr[0];
            int n1 = 1;
            int n2 = 0;

            for (int i = 1; i <n; i++) {
                if (arr[i] == seg1[n1-1]) {
                    if (n2 == 0 || seg2[n2-1] != arr[i]) {
                        seg2[n2] = arr[i];
                        n2 +=1;

                    }
                }
                else {
                    seg1[n1] = arr[i];
                    n1 += 1;
                }
            }

            return n1+n2;

        }

    }
}