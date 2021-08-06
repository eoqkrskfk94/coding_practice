import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
		int K = in.nextInt();

        int[] coins = new int[N];

        for(int i = 0; i < N; i++){
            coins[i] = in.nextInt();
        }

        int totalCount = 0;

        for(int i = N -1; i >= 0; i--){

            if(coins[i] <= K) {
                int temp = K/coins[i];

                totalCount += temp;
                K -= coins[i] * temp;
            }
        }

        System.out.println(totalCount);
    }
}