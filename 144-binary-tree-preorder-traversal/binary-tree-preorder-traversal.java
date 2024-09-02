/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        preor(root,ans);
        return ans;
    }
    private void preor(TreeNode node,List<Integer> ans){
        if (node == null ){
            return ;
        }
        ans.add(node.val);
        preor(node.left,ans);
        preor(node.right, ans);
    }
}