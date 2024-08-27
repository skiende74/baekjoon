import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static boolean[][] dp;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		dp = new boolean[k+1][x*k+1];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			arr[i] = a;
		}
		
		for(int p : arr) { //dp[i][j] i개일때 j가 가능한가
			knapsack(p,k,x);
		}
		int ans = 0;
		for(int i = 0; i <= x*k; i++) {
			if(dp[k][i]) {
				ans = Math.max(ans, i*(x*k-i));
			}
		}
		System.out.println(ans);
	}
	static void knapsack(int p, int k, int x) {
		for(int i = k-1; i >= 1; i--) {
			for(int j = x*k; j >= p; j--) {
				dp[i+1][j] = dp[i+1][j] || dp[i][j-p]; //j-p를 뺀 값이 있다면
			}
		}
		
		dp[1][p] = true;
	}
}