class Solution {
    public boolean checkValidString(String s) {
        int min = 0;
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                min += 1;
                max += 1;
            } else if (s.charAt(i) == ')') {
                min -= 1;
                max -= 1;
            } else { // s.charAt(i) == '*'
                min -= 1;
                max += 1;
            }

            // Ensure min doesn't go negative
            if (min < 0) {
                min = 0;
            }

            // If max is negative, too many ')' so it's invalid
            if (max < 0) {
                return false;
            }
        }

        // If min is 0, all parentheses are balanced
        return min == 0;
    }
}
