import java.util.*;

public class Alice{

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
        	String s = sc.next();
        	System.out.println(Game(s));
        }
    }


    private static String Game(String s){

    	boolean isAlice = true;
    	String ans = "";
    	for (int i = 0; i < s.length(); i++) {

    		if (isAlice == true) {
    			if (s.charAt(i) == 'a') {
    				ans = ans + "b";
    			}

    			else {
    				ans = ans+"a";
    			}
                isAlice = false;
    		}

    		else {
    			if (s.charAt(i) == 'z') {
    				ans = ans + "y";
    			}

    			else {
    				ans = ans+"z";
    			}
                isAlice = true;
    		}

    	}

    	return ans;
    }
}