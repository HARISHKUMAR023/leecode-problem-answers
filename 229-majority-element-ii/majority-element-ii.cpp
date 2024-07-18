class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
         int n = nums.size();
        int t = n / 3;
        std::vector<int> ans;
        std::unordered_map<int, int> my;

        for (int i : nums) {
            my[i]++;
        }

        for (auto& pair : my) {
            if (pair.second > t) {
                ans.push_back(pair.first);
            }
        }

        return ans;
    }
};