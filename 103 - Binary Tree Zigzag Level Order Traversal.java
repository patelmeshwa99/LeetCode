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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
         List<List<Integer>> ans = new ArrayList<>();
        if(root==null){
            return ans;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int counter=0;
        while(!q.isEmpty()){
            counter++;
            int size = q.size();
            List<Integer> l = new ArrayList<>();

            for(int i=0; i<size; i++){
                TreeNode tn = q.remove();
                l.add(tn.val);
                if(tn.left != null){
                    q.add(tn.left);
                }
                if(tn.right != null){
                    q.add(tn.right);
                }
            }
            if(counter%2==0)
            {
                Collections.reverse(l);
            }
            ans.add(l);
        }
        return ans;
    }
}