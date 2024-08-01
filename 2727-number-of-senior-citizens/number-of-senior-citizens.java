class Solution {
    public int countSeniors(String[] details) {
       int ans = 0;
        for (int i = 0; i < details.length; i++) {
            // Extract the substring for the age and convert it to an integer
            int age = Integer.parseInt(details[i].substring(11, 13));
            if (age > 60) {
                ans++;
            }
        }
        return ans;
    }
}