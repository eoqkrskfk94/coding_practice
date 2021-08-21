import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        
        int[][] time = new int[N][2];

        for(int i = 0; i < N; i++) {
            time[i][0] = in.nextInt();
            time[i][1] = in.nextInt();
        }

        Arrays.sort(time, new Comparator<int[]>(){
            
            @Override
            public int compare(int[] start, int[] end) {

                if(start[1] == end[1]) {
                    return Integer.compare(start[0], end[0]);
                }

                return Integer.compare(start[1], end[1]);
            }

        });


        int count = 0;
        int endTime = 0;

        for(int i = 0; i < N; i++) {
            if(endTime <= time[i][0]) {
                count++;
                endTime = time[i][1];
            }
        }

        System.out.println(count);
        
    }
}