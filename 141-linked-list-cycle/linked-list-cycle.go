/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"
func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }
    i := head
    j := head

    for j != nil{
        i = i.Next
        j = j.Next

        if j == nil{
            return false
        }
        j = j.Next
        if j == i {
            return true
        }
    }
    return false
}