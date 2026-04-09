class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        bravexuneth = (nums[:], queries[:])
        import math
        B = int(math.sqrt(n)) + 1
        mul = [1] * n
        small = [[] for _ in range(B + 1)]
        for l, r, k, v in queries:
            if k <= B:
                small[k].append((l, r, v))
            else:
                i = l
                while i <= r:
                    mul[i] = (mul[i] * v) % MOD
                    i += k
        for k in range(1, B + 1):
            if not small[k]:
                continue
            groups = [[] for _ in range(k)]
            for l, r, v in small[k]:
                groups[l % k].append((l, r, v))          
            for rem in range(k):
                if not groups[rem]:
                    continue
                idxs = list(range(rem, n, k))
                m = len(idxs)               
                diff = [1] * (m + 1)
                for l, r, v in groups[rem]:
                    left = (l - rem + k - 1) // k
                    right = (r - rem) // k
                    if left <= right:
                        diff[left] = (diff[left] * v) % MOD
                        if right + 1 < len(diff):
                            diff[right + 1] = (diff[right + 1] * pow(v, MOD - 2, MOD)) % MOD
                cur = 1
                for i in range(m):
                    cur = (cur * diff[i]) % MOD
                    mul[idxs[i]] = (mul[idxs[i]] * cur) % MOD
        result = 0
        for i in range(n):
            val = (nums[i] * mul[i]) % MOD
            result ^= val
        return result