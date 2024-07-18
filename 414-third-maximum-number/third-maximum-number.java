class Solution {
    public int thirdMax(int[] nums) {
        TreeSet<Integer> uniqueNums = new TreeSet<>(Collections.reverseOrder());
        
       
        for (int num : nums) {
            uniqueNums.add(num);
        }
        
        List<Integer> sortedList = new ArrayList<>(uniqueNums);
        
        
        if (sortedList.size() < 3) {
            return sortedList.get(0);
        } else {
            return sortedList.get(2); 
        }
    }
}