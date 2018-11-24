public class cubicTime {

  // Time complexity: O(n^3)
  // Space complexity: O(1)
  public static void print2DArray(int [][] m) {
    for(int i = 0; i < m.length; i++) {
      for(int j = 0; j < m[0].length; j++) {
        for(int k = 0; k < m[0].length; k++) {
          System.out.print(m[i][j] + ",");
        }
      }
      System.out.println();
    }
  }
  public static void main(String[] args) {
    int [][] m = new int[3][3];
    m[0][0] = 1;
    m[0][1] = 2;
    m[0][2] = 3;
    m[1][0] = 4;
    m[1][1] = 5;
    m[1][2] = 6;
    m[2][0] = 7;
    m[2][1] = 8;
    m[2][2] = 9;
    print2DArray(m);
  }
}