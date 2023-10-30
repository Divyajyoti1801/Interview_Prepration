package Princeton_University_Algorithm.algorithm_1.union_find;

class Quick_Find {
    private int[] id;

    // Constructor
    public Quick_Find(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q];
    }

    public void union(int p, int q) {

    }

    public static void main(String[] args) {

    }
}