import java.util.*;

public class Mountain{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){

        	int n = sc.nextInt();
        	int k = sc.nextInt();

        	int[] moun = new int[n];

        	for (int i =0; i < n; i++){
        		moun[i] = sc.nextInt();
        	}

        	System.out.println(boulder(moun, k));
        }

	} 

	private static int boulder(int[] moun, int k) {

		int i = 1;
		int pos = -1;
		

		while (i <= k) {
			pos = 0;

			while(pos < moun.length){

				if (pos == moun.length -1) {
					return -1;
				}

				if(moun[pos] >= moun[pos+1]) {
					pos += 1;
				}

				else {
					moun[pos] += 1;
					break;
				}
			}
				
			i += 1;
		}

		if (pos >= moun.length -1){
			return -1;
		}
		return pos+1;

	}
}