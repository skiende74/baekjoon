import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int N;
    static int M;
    static int cnt = 0;
    static void dfs(int v) {
        for (int i : graph[v]) {
            if(!visited[i]) {
                visited[i] = true;
                cnt += 1;
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        N = s.nextInt();
        M = s.nextInt();
        visited = new boolean[N+1];
        graph = new ArrayList[N+1];
        for(int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int k = 0; k < M; k++) {
            int i = s.nextInt();
            int j = s.nextInt();
            graph[i].add(j);
            graph[j].add(i);
        }
        visited[1] = true;
        dfs(1);
        System.out.println(cnt);
        s.close();
    }
}