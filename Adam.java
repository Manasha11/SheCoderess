import java.util.*;
public class Adam {
    static int reverseDigits(int num)
    {
        int rev = 0;
        while (num > 0)
        {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        return rev;
    }
 
    static int square(int num)
    {
        return (num * num);
    }
 
    static boolean checkAdamNumber(int num)
    {
        int a = square(num);
        int b = square(reverseDigits(num));
         
        if (a == reverseDigits(b))
        return true;
        return false;       
    }
 
    public static void main(String[] args)
    {
		Scanner scanner = new Scanner(System.in);
		int num = scanner.nextInt();
         
        if (checkAdamNumber(num))
        System.out.println("yes");
        else
        System.out.println("no");    
    }
 
}
