/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
          let diametr =0;
        function dfs(node){
    if (!node) return 0;
    
    let leftDepth = dfs(node.left)
    let rightDepth= dfs(node.right)
    let d = leftDepth + rightDepth
    diametr = Math.max(d, diametr)
    return Math.max(leftDepth, rightDepth)+1;
  }
  dfs(root);
  return diametr;
    }
}
