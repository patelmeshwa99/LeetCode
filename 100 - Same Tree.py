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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if((p==null && q!=null) || (p!=null && q==null)){
            return false;
        }
        if(p==null && q==null){
            return true;
        }
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();

        q1.add(p);
        q2.add(q);
        
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();

        while(!q1.isEmpty()){
            int size = q1.size();

            for(int i=0; i<size; i++){
                TreeNode tn = q1.remove();
                l1.add(tn.val);
                if(tn.left != null){
                    q1.add(tn.left);
                }
                else
                {
                    l1.add(null);
                    l1.add(null);
                }
                if(tn.right != null){
                    q1.add(tn.right);
                }
                else
                {
                    l1.add(null);
                }
            }
        }
        while(!q2.isEmpty()){
            int size = q2.size();

            for(int i=0; i<size; i++){
                TreeNode tn = q2.remove();
                l2.add(tn.val);
                if(tn.left != null){
                    q2.add(tn.left);
                }
                else
                {
                    l2.add(null);
                    l2.add(null);
                }
                if(tn.right != null){
                    q2.add(tn.right);
                }
                else{
                    l2.add(null);
                }
            }
        }
        return l1.equals(l2);
    }
}

