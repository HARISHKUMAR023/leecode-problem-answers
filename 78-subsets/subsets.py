class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]] 
     
        for num in nums:
            new_subsets = []  # Create a list to hold new subsets
            for curr_subset in ans:
                new_subset = curr_subset + [num]  # Form a new subset by adding `num`
                new_subsets.append(new_subset)    # Append the new subset to `new_subsets`
            ans.extend(new_subsets)  # Add new subsets to `ans`

        return ans
