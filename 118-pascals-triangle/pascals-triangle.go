func generate(numRows int) [][]int {
	var out = make([][]int, 0)

	for i := 1; i <= numRows; i++ {
		if i == 1 {
			out = append(out, []int{1})
			continue
		}
		ans := []int{1}

		for j := 0; j < len(out[len(out)-1])-1; j++ {
			ans = append(ans, out[len(out)-1][j]+out[len(out)-1][j+1])
		}
		ans = append(ans, 1)
		out = append(out, ans)
	}
	return out
}