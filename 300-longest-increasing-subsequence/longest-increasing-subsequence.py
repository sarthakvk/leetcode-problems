class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        n = len(nums)

        for i in range(1,n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                s = 0
                e = len(ans) - 1

                while s < e:
                    m = (s+e)//2

                    if ans[m] < nums[i]:
                        s = m + 1
                    else:
                        e = m
                
                ans[s] = nums[i]
        return len(ans)



        