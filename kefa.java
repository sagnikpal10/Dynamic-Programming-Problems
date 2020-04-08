import java.util.*;

public class kefa{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int s = sc.nextInt();
        
        String ans = "";
        int count = m;
        if(s == 0){
            System.out.print(-1);
            System.out.print(" " + -1);
        }
        else{
            for(int num=9; num>= 1 && count > 0; num--){
                for(int i=m-1; i>=1; i--){
                    if(num*i <= s && s > 9 && s > count){
                        // System.out.println(s);
                        for(int j=0; j<i; j++){
                            ans += Integer.toString(num);
                        }
                        // System.out.println(num + " : " + i);
                        s -= num*i;
                        count-=i;
                        // System.out.println(count);
                        break;
                    }
                    if(s <= 9){
                        // System.out.println((s - count + 1) + " : " + 1);
                        ans += Integer.toString(s - count + 1);
                        // System.out.println(1 + " : " + (count - 1));
                        for(int j=0; j<count - 1; j++){
                            ans += Integer.toString(1);
                        }
                        count = 0;
                        s = 0;
                        break;
                    }
                    if(s > 9 && s == count){
                        // System.out.println(1 + " : " + count);
                        for(int j=0; j<count; j++){
                            ans += Integer.toString(1);
                        }
                        s = 0;
                    }
                }
            }
            if(s == 0){
                System.out.println(new StringBuffer(ans).reverse()+ " "+ ans);
            }
            else{
                System.out.print(-1);
                System.out.print(" " + -1);
            }
        }
        
        // System.out.println(ans);
        
        
        
    }
}
