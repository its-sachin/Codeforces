import java.util.*;


public class q3{
    
    public static void main(String[] args) {
        int N;

        Scanner scn = new Scanner(System.in);

        N = scn.nextInt();

        int i = 0;
        int count = 0;
        int sum = 0;

        while(i<N) {

            sum += scn.nextInt();

            i += 1;

        }

        System.out.println(count);

    }

}