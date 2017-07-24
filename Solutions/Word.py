import java.util.*;
class word{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		String inp = scanner.nextLine();
		String[] wa = inp.split("\\W+");
		System.out.println(wa.length);
	}
}
