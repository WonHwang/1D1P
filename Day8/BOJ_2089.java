// 1D1P Day8 BOJ 2089번 -2진수 문제 - 2020.11.12

package Day8;

import java.util.Scanner;

public class BOJ_2089{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String answer = "";
        if (N == 0) answer = "0";
        while(N != 0){
            if (N%-2 == -1){
                N = (N/-2) + 1;
                answer = "1" + answer;
            }
            else if (N%-2 == 0){
                N = N/-2;
                answer = "0" + answer;
            }
            else{
                N = N/-2;
                answer = "1" + answer;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}