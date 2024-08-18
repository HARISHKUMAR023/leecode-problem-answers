
class Solution {
public:
    int findLUSlength(std::string a, std::string b) {
        if (a == b) {
            return -1;
        } else {
            return std::max(a.size(), b.size());
        }
    }
};
