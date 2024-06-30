import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int T = s.nextInt();
        for (int k = 0; k < T; k++) {
            int N = s.nextInt();
            int dp[] = new int[N + 1];
            dp[0] = 1;
            dp[1] = 1;
            if (N<=1){
                System.out.println(dp[N]);
                continue;
            }
            dp[2] = 2;
            for (int i = 3; i <= N; i++) {
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
            }
            System.out.println(dp[N]);
        }
        s.close();
    }
}