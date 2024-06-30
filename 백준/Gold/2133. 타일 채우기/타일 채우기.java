import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int dp[] = new int[100];

        dp[0] = 1;
        for (int i = 2; i <= N; i += 2) {
            dp[i] = dp[i - 2] * 3;
            for (int j = 0; j <= i - 4; j += 2) {
                dp[i] += 2 * dp[j];
            }
        }
        System.out.println(dp[N]);

        s.close();
    }
}
