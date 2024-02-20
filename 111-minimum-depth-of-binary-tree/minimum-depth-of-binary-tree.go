/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }

    if root.Left == nil && root.Right == nil {
        return 1
    }

    left := math.MaxInt
    if root.Left != nil {
        left = minDepth(root.Left)
    }

    right := math.MaxInt
    if root.Right != nil {
        right = minDepth(root.Right)
    }

    return 1 + min(left, right)
    
}