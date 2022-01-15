import java.util.*;

public class Space{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	int px = sc.nextInt();
        	int py = sc.nextInt();
        	String s = sc.next();

        	if (check(px, py, s)) {
        		System.out.println("YES");
        	}

        	else {
        		System.out.println("NO");
        	}


        }
	}

	private static boolean check(int px, int py, String s) {
		String leftOut = "";
		int x = 0;
		int y = 0;

		char u = 85;
		char d = 68;
		char r = 82;
		char l = 76;

		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == u && py >= 0 ) {
				if (y == py) {
					leftOut = leftOut + "U";
				}
				else {
					y += 1;
				}
			}

			if (s.charAt(i) == d && py <= 0 ) {
				if (y == py) {
					leftOut = leftOut + "D";
				}
				else {
					y -= 1;
				}
			}

			if (s.charAt(i) == r && px >= 0 ) {
				if (x == px) {
					leftOut = leftOut + "R";
				}
				else {
					x += 1;
				}
			}

			if (s.charAt(i) == l && px <= 0 ) {
				if (x == px) {
					leftOut = leftOut + "L";
				}
				else {
					x -= 1;
				}
			}
		}

		if (x == px && y == py) {
			return true;
		}
		return false;

	}

}