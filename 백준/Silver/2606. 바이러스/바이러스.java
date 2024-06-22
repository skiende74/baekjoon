import java.util.*;

public class Main{
    public static ArrayList<ArrayList<Integer>> graphs = new ArrayList<>();
    static boolean visited[];
    static int cnt = 0;
    static void dfs(int v){
        for(int i : graphs.get(v)) {
            if (!visited[i]) {
                visited[i] = true;
                cnt += 1;
                dfs(i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int M = s.nextInt();
        visited = new boolean[N+1];
        visited[0] = true;
        visited[1] = true;

        for(int i = 0; i < N + 1; i++) {
            graphs.add(new ArrayList<Integer>());
        }
        for(int i = 0; i < M; i++) {
            int j = s.nextInt();
            int k = s.nextInt();
            graphs.get(j).add(k);
            graphs.get(k).add(j);
        }
        dfs(1);
        System.out.println(cnt);
    }
}