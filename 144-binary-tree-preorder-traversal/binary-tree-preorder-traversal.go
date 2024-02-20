/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func pre(root *TreeNode, ans []int) []int {
    if root == nil{
        return ans
    }
    ans = append(ans, root.Val)
    ans = pre(root.Left, ans)
    ans = pre(root.Right, ans)
    return ans
}

func preorderTraversal(root *TreeNode) []int {
    var ans = []int{}
    ans = pre(root, ans)
    return ans
}