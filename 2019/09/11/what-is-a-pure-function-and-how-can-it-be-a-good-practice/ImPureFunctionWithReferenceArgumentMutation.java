public class ImPureFunctionWithReferenceArgumentMutation {
  public static void append(ArrayList<Integer> list, Integer a) {
    list.add(a);
  }
  public static void main(String [] args) {
    ArrayList<Integer> list = new ArrayList<>(Arrays.asList(1, 3, 5, 7, 9));
    System.out.println(list.size()); // 5
    append(list, 11);
    System.out.println(list.size()); // 6
  }
}