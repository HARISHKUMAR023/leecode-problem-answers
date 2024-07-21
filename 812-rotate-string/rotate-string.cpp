class Solution {
public:
    bool rotateString(string s, string goal) {
          if (s.length() != goal.length()) {
            return false;
        }

        string my = s;

        for (size_t i = 0; i < my.length(); ++i) {
            if (my == goal) {
                return true;
            }
            rotate(my.begin(), my.begin() + 1, my.end());
        }

        return false;
    }
};