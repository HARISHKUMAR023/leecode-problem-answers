import java.util.List;

class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int min_val = arrays.get(0).get(0); // Access first element of the first list
        int max_val = arrays.get(0).get(arrays.get(0).size() - 1); // Access last element of the first list
        int maxi = 0;

        for (int i = 1; i < arrays.size(); i++) { // Start loop from 1, since we initialized with 0th list
            int c_min = arrays.get(i).get(0); // Access first element of current list
            int c_max = arrays.get(i).get(arrays.get(i).size() - 1); // Access last element of current list
            
            // Calculate the maximum distance considering the current list
            maxi = Math.max(maxi, Math.max(Math.abs(min_val - c_max), Math.abs(max_val - c_min)));

            // Update min_val and max_val with the current list's values
            min_val = Math.min(min_val, c_min);
            max_val = Math.max(max_val, c_max);
        }
        return maxi;
    }
}
