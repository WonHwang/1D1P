// 1D1P Day8 BOJ 11576번 Base Conversion 문제 - 2020.11.12

package Day8;

import java.util.Scanner;

public class BOJ_11576{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A, B, numofdigit;
        int[] digits = new int[25];
        A = sc.nextInt();
        B = sc.nextInt();
        numofdigit = sc.nextInt();
        for (int i=0; i<25; i++) digits[i] = 0;
        for (int i=0; i<numofdigit; i++) digits[i] = sc.nextInt();

        int tmp = 1;
        int decimal = 0;
        for (int i=numofdigit-1; i>=0; i--){
            decimal += tmp * digits[i];
            tmp *= A;
        }
        for (int i=0; i<25; i++) digits[i] = 0;
        tmp = 0;
        while (decimal != 0){
            digits[tmp++] = decimal % B;
            decimal /= B;
        }
        for (int i=tmp-1; i>=0; i--) System.out.print(digits[i] + " ");
        sc.close();
    }
}