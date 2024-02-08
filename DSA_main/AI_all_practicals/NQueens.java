public class NQueens {
    // This is the actually the creation of the array of num of row where the queens
    // are prensented
    private int[] queens;
    private int numSolutions;

    public void solveNQueens(int n) {
        queens = new int[n];
        numSolutions = 0;
        backtrack(0, n);
    }

    private void backtrack(int row, int n) {
        if (row == n) {
            numSolutions++;
            printSolution();
            return;
        }
        // The recursive nature of the backtrack method allows the algorithm to explore
        // all possible combinations of queen placements,
        // ensuring that all valid solutions are found.

        for (int col = 0; col < n; col++) {
            queens[row] = col;
            if (isSafe(row, col)) {
                // this is the actually the method for traversing throught the all rows and
                // columns
                backtrack(row + 1, n);
            }
        }
    }

    private boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            // The second condition, queens[i] - col == i - row,
            // checks if there is a queen placed on the same diagonal (top-left to
            // bottom-right) as the current position.

            // The third condition, queens[i] - col == row - i,
            // checks if there is a queen placed on the same anti-diagonal (top-right to
            // bottom-left) as the current position.

            // this is the actually of the way to check the any one of the condition
            if (queens[i] == col || queens[i] - col == i - row || queens[i] - col == row - i) {
                return false;
            }
        }
        return true;
    }

    // This is actually the method for the creting the board confiurgation

    private void printSolution() {
        System.out.println("Solution " + numSolutions + ":");

        // This for loop iterates throught the number of rows and the columns

        for (int i = 0; i < queens.length; i++) {
            for (int j = 0; j < queens.length; j++) {

                // When the queen are present in the particular row print the queen

                if (queens[i] == j) {
                    System.out.print(" Q ");
                } else {
                    System.out.print(" 0 ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {

        // This is the actually the creating the instance of the class

        NQueens nQueens = new NQueens();

        int n = 4; // Number of queens (board size)

        nQueens.solveNQueens(n);
    }
}
