import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int dp[] = new int[100];
        if (N % 2 == 1) {
            System.out.println(0);
            s.close();
            return;
        }

        dp[0] = 1;
        dp[2] = 3;
        dp[4] = 9 + 2;
        for (int i = 6; i <= N; i += 2) {
            dp[i] = dp[i - 2] * 3;
            for (int j = 0; j <= i - 4; j += 2) {
                dp[i] += 2 * dp[j];
            }
        }
        System.out.println(dp[N]);

        s.close();
    }
}
