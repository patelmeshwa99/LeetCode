class Solution {
    
    public int totalSteps(int[] nums) {
        return makeArrayNonDecreasing(nums);
    }

    private int makeArrayNonDecreasing(int[] numsProvided) {
        Stack<Integer> intStack = new Stack<>();
        boolean workMore = true;
        int steps = 0;
        while (workMore) {
            Object[] nums;
            if (steps == 0) {
                Integer[] boxedArray = IntStream.of(numsProvided)
                                .boxed()
                                .toArray(Integer[]::new);
                nums = boxedArray;
            } else {
                nums = intStack.toArray();
            }
            steps += 1;
            // Object[] nums = intStack.toArray();
            intStack.clear();
            for (int i=1; i<nums.length; i++) {
                if ((Integer)nums[i-1] > (Integer)nums[i]) {
                    if (i == 1) {
                        intStack.push((Integer)nums[i-1]);
                    }
                } else {
                    if (i == 1) {
                        intStack.push((Integer)nums[i-1]);
                    }
                    intStack.push((Integer)nums[i]);
                }
            }
            if (intStack.size() == nums.length || intStack.size() == 0) {
                workMore = false;
            }
        }
        return steps-1;
    }

    private Stack<Integer> convertArrayToStack(int[] nums) {
        Stack<Integer> intStack = new Stack<>();
        for (int i=0; i<nums.length; i++) {
            intStack.push(nums[i]);
        }
        return intStack;
    }
}