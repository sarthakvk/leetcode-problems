class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dp(idx, current_set, can_change):
            if idx >= len(s):
                return 0
            
            character_idx = ord(s[idx]) - ord('a')

            cs_updated = current_set | 1 << character_idx
            ds_count = cs_updated.bit_count()

            if ds_count > k:
                res = 1 + dp(idx+1, 1 << character_idx, can_change)
            else:
                res = dp(idx+1, cs_updated, can_change)

            if can_change:
                for ch_idx in range(26):
                    new_set = current_set | (1 << ch_idx)
                    ds_count = new_set.bit_count()

                    if ds_count > k:
                        res = max(res, 1+dp(idx+1, 1<<ch_idx, False))
                    else:
                        res = max(res, dp(idx+1, new_set, False))
            
            return res
        return dp(0, 0, True)+1