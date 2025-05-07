class Solution {
    public int search(int[] nums, int target) {
        int beg = 0;
        int end = nums.length-1;
        int midIndex = 0;
        
        while (beg <= end) {
            midIndex = (beg + end) / 2;
            if (nums[midIndex] == target) {
                return midIndex;
            } else if (target < nums[midIndex]) {
                if(target > nums[beg]){
                    end = decrementPointer(midIndex);   
                } else if(target < nums[beg]) {
                    if(target < nums[end]) {
                        beg = incrementPointer(beg);
                    } else {
                        beg = incrementPointer(midIndex);        
                    }
                } else {
                    end = decrementPointer(midIndex);
                }
            } else {
                  if(target > nums[beg]){
                     if (target > nums[end]) {
                        end = decrementPointer(end);             
                     } else {
                         beg = incrementPointer(midIndex);        
                     }
                    
                } else if (target < nums[beg]) {
                    beg = incrementPointer(midIndex);        
                } else {
                    end = decrementPointer(midIndex);             
                }
            }
        }
        return -1;
    }
    
    private int incrementPointer(int pointer) {
        return pointer += 1;
    }
    
    private int decrementPointer(int pointer) {
        return pointer -= 1;
    }
}


// BEST
/*
public class Main
{
	public static void main(String[] args) {
		int beg = 0;
		int[] nums = new int[]{4,5,6,7,0,1,2};
        int end = nums.length-1;
        int midIndex = 0;
        int target = 4;
        
        while (beg <= end) {
            midIndex = (beg + end) / 2;
            if (nums[midIndex] == target) {
                System.out.println(midIndex);
            } 
            if (nums[midIndex] >= nums[beg]) {
                if (target > nums[midIndex] || target < nums[beg]) {
                    beg = midIndex + 1;
                } else {
                    end = midIndex - 1;
                }
            } else {
                if (target < nums[midIndex] || target > nums[end]) {
                    end = midIndex - 1;
                } else {
                    beg = midIndex + 1;
                }
            }
        }
        System.out.println("-1");
	}
}
*/