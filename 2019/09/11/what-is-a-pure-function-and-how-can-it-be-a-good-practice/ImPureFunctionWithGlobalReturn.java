public class ImPureFunctionWithGlobalReturn {
  public static int accessImpureAddFunctionCount = 0;
  public static int impureAdd(int a, int b) {
    accessImpureAddFunctionCount++;
    return a + b;
  }
  public static int getAccessImpureAddFunctionCount() {
    return accessImpureAddFunctionCount;
  }
  public static void main(String [] args) {
    int c = impureAdd(10, 5);
    System.out.println(c); // 15
    c = impureAdd(5, 20);
    System.out.println(c); // 25
    System.out.println(getAccessImpureAddFunctionCount()); // 2
  }
}