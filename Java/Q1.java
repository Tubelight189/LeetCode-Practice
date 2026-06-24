package LC;

import java.util.HashMap;

public class Q1 {
    static int[] sum(int[] arr,int s){
        HashMap<Integer,Integer>map=new HashMap<>();
        int[]ans=new int[2];
        for (int i=0;i< arr.length;i++) {
            if (map.containsKey(s-arr[i])){
                ans[0]=map.get(s-arr[i]);
                ans[1]=i;
                return ans;
            }
            else {map.put(arr[i],i);}
            }return ans;
    }
    public static void main(String[] args) {
int[] arr={2,7,11,15};int[] k=sum(arr,9);
        System.out.println(k);
}}
