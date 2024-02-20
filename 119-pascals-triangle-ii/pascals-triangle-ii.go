func getRow(rowIndex int) []int {
    out := []int{}
    for i := 0; i <= rowIndex; i++ {
        if i < 2{
            out = append(out, 1)
            continue
        }
        new := []int{1}

        for j := 0; j < len(out)-1; j++{
            new = append(new, out[j]+out[j+1])
        }
        new = append(new, 1)
        out = new
    }
    return out
}