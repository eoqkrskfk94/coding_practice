import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

class Main{

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        Integer[] ropes = new Integer[N];
        int possibleWeight = 0;

        for(int i = 0; i < N; i++) {
            ropes[i] = in.nextInt();
        }

        Arrays.sort(ropes, Collections.reverseOrder());

        for(int i = 0; i < N; i++) {
            int temp = ropes[i] * (i+1);

            if(possibleWeight < temp) possibleWeight = temp;
        }

        System.out.println(possibleWeight);

    }

}