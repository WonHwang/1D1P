// 1D1P Day5 BOJ 2902번 KMP는 왜 KMP일까? 문제 - 2020.11.09
package Day5;

import java.util.Scanner;

public class BOJ_2902 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String names = sc.nextLine();
        String answer = "";
        answer += names.charAt(0);
        for (int i=1; i<names.length(); i++){
            if (names.charAt(i) == '-') answer += names.charAt(i+1);
        }
        System.out.println(answer);
        sc.close();
    }
}