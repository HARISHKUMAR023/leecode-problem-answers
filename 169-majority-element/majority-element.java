class Solution {
    public int majorityElement(int[] nums) {
        
        Map<Integer, Integer> countMap = new HashMap<>();
        int majorityCount = nums.length / 2;
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            
            if (countMap.get(num) > majorityCount) {
                return num;
            }
        }
        return -1;
    }
}