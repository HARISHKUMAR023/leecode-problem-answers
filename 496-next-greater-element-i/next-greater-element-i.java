class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> my = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) {
            my.put(nums2[i], i);
        }
        int[] ans = new int[nums1.length];
        for (int j = 0; j < nums1.length; j++) {
            boolean found = false;

            // Start searching in nums2 from the index of nums1[j]
            for (int p = my.get(nums1[j]); p < nums2.length; p++) {
                if (nums2[p] > nums1[j]) {  
                    ans[j] = nums2[p];
                    found = true;  
                    break;
                }
            }

            // If no greater element is found, set -1
            if (!found) {
                ans[j] = -1;
            }
        }

        return ans;  // Return 
    

    }
}