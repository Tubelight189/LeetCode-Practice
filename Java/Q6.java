package LC;

public class Q6 {
    static String zz(String a,int r){
        String s="";
        char[][] m = new char[r][a.length()/2];
        for (int i=0;i<a.length();i++) {
            int j=0;
            if (i==r){j++;i=i+r;}
                m[i][j]=a.charAt(i);

        }
        for (int i=0;i< r;i++) {
            for (int j = 0; j < a.length()/2; j++){
s=s+m[i][j];}
        }return s;
    }

    public static void main(String[] args) {
       String a="PAYPALISHIRING";

        System.out.println(zz(a,3));

    }
}
