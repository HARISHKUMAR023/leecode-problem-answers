class Solution {
    public boolean rotateString(String s, String goal) {
         if (s.length() != goal.length()) {
            return false;
        }
        
        String b = s;
        char[] my = b.toCharArray();
        
        for (int i = 0; i < my.length; i++) {
            if (new String(my).equals(goal)) {
                return true;
            }
            char firstChar = my[0];
            System.arraycopy(my, 1, my, 0, my.length - 1);
            my[my.length - 1] = firstChar;
        }
        
        return false;
    }
}