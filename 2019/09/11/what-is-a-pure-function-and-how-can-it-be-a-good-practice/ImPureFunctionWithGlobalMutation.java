public class ImPureFunctionWithGlobalMutation {
  public static int accessAddFunctionCount = 0;
  public static int add(int a, int b) {
    accessAddFunctionCount++;
    return a + b;
  }
  public static void main(String [] args) {
    int c = add(10, 5);
    System.out.println(c); // 15
    c = add(5, 20);
    System.out.println(c); // 25
  }
}