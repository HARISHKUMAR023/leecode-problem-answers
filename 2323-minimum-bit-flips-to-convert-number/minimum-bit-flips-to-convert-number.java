class Solution {
    public int minBitFlips(int start, int goal) {
        int  r= start^goal;
         int v=Integer.bitCount(r);
        return v;
    }
}