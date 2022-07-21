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
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null) {
            return new ArrayList<>();
        }
        List<Integer> inorderList = new ArrayList<>();
        
        // Inorder Travsersal of left first
        if(root.left != null) {
            inorderList.addAll(inorderTraversal(root.left));  
        } 
        
        // Then the root
        inorderList.add(root.val);
        
        // At last, right
        if(root.right != null) {
            inorderList.addAll(inorderTraversal(root.right));
        }
        return inorderList;
    }
}


// BEST SOLUTION
/*class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res;
    }

    public void helper(TreeNode root, List<Integer> res) {
        if (root != null) {
            helper(root.left, res);
            res.add(root.val);
            helper(root.right, res);
        }
    }
}*/