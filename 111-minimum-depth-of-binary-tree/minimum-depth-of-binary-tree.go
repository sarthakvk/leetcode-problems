/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func min(a, b int) int {
    if a < b{
        return a
    }
    return b
}

func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    } else if root.Left == nil && root.Right == nil {
        return 1
    }

    dr := (int)(1e6)
    dl := (int)(1e6)
    if root.Left != nil{
        dl = minDepth(root.Left)
    }

    if root.Right != nil {
        dr = minDepth(root.Right)
    }

    return min(dr, dl) + 1
}
