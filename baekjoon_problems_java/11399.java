import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {
     
        Scanner in = new Scanner(System.in);
        int sum = 0;
        int min = 0;

        int N = in.nextInt();

        int[] times = new int[N];

        for(int i = 0; i < N; i++){
            times[i] = in.nextInt();
        }

        Arrays.sort(times);

        for(int i = 0; i < N; i++){
            sum += times[i];
            min += sum;
        }

        System.out.println(min);
    }
}