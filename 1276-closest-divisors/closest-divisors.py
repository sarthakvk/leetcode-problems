class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def getDivisors(num):
            ans = [(1, num)]
            sqrt = int(pow(num, 0.5))
            for i in range(2, sqrt+1):
                if num%i == 0:
                    ans.append((i, num//i))
            return ans

        def closest(divs):
            ans = [1, divs[0][1]]
            diff = abs(1-ans[1])
            for i in divs:
                if abs(i[0]-i[1]) < diff:
                    diff = abs(i[0]-i[1])
                    ans = i
            return ans


        n1 = num+1
        n2 = n1+1

        d1 = getDivisors(n1)
        d2 = getDivisors(n2)

        c1 = closest(d1)
        c2 = closest(d2)

        if abs(c1[0]-c1[1]) < abs(c2[0]-c2[1]):
            return c1
        else:
            return c2
        