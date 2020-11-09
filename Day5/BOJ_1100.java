// 1D1P Day5 BOJ 1100번 하얀 칸 문제 - 2020.11.09

package Day5;

import java.util.Scanner;

public class BOJ_1100 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] chess = new String[8];
        for (int i=0; i<8; i++){
            chess[i] = sc.nextLine();
        }
        int answer = 0;
        for (int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                if ((i+j) % 2 == 0 && chess[i].charAt(j) == 'F') answer++;
            }
        }
        System.out.println(answer);
        sc.close();
    }
}