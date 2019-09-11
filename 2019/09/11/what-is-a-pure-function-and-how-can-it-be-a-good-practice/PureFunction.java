public class PureFunction {
  public static int add(int a, int b) {
    return a + b;
  }
  public static void main(String [] args) {
    int c = add(10, 5);
    System.out.println(c); // 15
  }
}