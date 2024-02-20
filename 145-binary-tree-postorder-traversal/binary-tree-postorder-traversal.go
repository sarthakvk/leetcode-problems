/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func post(root *TreeNode, ans []int) []int {
    if root == nil{
        return ans
    }

    ans = post(root.Left, ans)
    ans = post(root.Right, ans)
    ans = append(ans, root.Val)
    return ans
}

func postorderTraversal(root *TreeNode) []int {
    ans := []int{}
    ans = post(root, ans)
    return ans
}