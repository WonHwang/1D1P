// 1D1P Day6 BOJ 2914 저작권 문제 - 2020.11.10

package Day6;

import java.util.Scanner;

public class BOJ_2914{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int avg = sc.nextInt();
        System.out.println(number*(avg-1) + 1);
        sc.close();
    }
}