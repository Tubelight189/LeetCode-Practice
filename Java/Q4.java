package LC;
import java.util.Arrays;
public class Q4 {
    public void main(String[] args){
     double n;
    int[] nums1 = {1,2}, nums2 = {3,4};
              int[]  nums3=new int[nums1.length+ nums2.length];

        for (int i=0;i<nums1.length;i++) {
            nums3[i] = nums1[i];
        }

        for (int i= nums1.length;i< nums3.length;i++) {
            nums3[i]=nums2[i- nums1.length];
        }
        Arrays.sort(nums3);
        for (int i= 0;i< nums3.length;i++) {
            System.out.println(nums3[i]);
        }
        if(nums3.length%2==1) n=nums3[nums3.length/2];
        else n= (nums3[nums3.length/2]+nums3[(nums3.length/2)-1])/2;
        System.out.println((nums3[nums3.length/2]+nums3[(nums3.length/2)-1])/2F);
    }}
