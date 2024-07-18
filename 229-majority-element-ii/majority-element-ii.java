class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n = nums.length;
        int t = n / 3;
        List<Integer> ans = new ArrayList<>();
        Map<Integer, Integer> my = new HashMap<>();

        for (int i : nums) {
            my.put(i, my.getOrDefault(i, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : my.entrySet()) {
            if (entry.getValue() > t) {
                ans.add(entry.getKey());
            }
        }

        return ans;
        
    }
}