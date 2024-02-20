import (
    "strings"
    "unicode"
)

func isPalindrome(s string) bool {
    f := []string{}

    for _, v := range s {
        if unicode.IsLetter(v) || unicode.IsDigit(v) {
            f = append(f, strings.ToLower((string)(v)))
        }
    }
    i := 0
    j := len(f)-1

    for i < j {
        if f[i] != f[j]{
            return false
        }
        i++
        j--
    }
    return true
}