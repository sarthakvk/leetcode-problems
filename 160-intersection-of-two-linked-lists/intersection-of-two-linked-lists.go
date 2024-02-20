/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    l1 := 0
    l2 := 0
    t1 := headA
    t2 := headB
    tailA := headA
    tailB := headB

    for t1 != nil {
        tailA = t1
        t1 = t1.Next
        l1++
    }

    for t2 != nil {
        tailB = t2
        t2 = t2.Next
        l2++
    }

    if tailA != tailB {
        return nil
    }

    if l1 > l2{
        for i := 0; i < l1-l2; i++ {
            headA = headA.Next
        }
    }
    if l2 > l1 {
        for i := 0; i < l2-l1; i++ {
            headB = headB.Next
        }        
    }

    for headA != headB{
        headA = headA.Next
        headB = headB.Next
    }
    return headA
}