def longestOnes(nums, k):
        l = 0
        r = 0
        maxi = 0
        zeros = 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                maxi = max(maxi, r-l+1)
            r += 1
        return maxi