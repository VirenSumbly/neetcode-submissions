class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        m = 0

        for i in range(1, len(height)):
            m = max(m, height[i - 1])
            left.append(m)

        right = [0]
        p = 0

        for i in range(len(height) - 2, -1, -1):
            p = max(p, height[i + 1])
            right.append(p)

        right.reverse()

        ans = 0

        for i in range(len(height)):
            diff = min(left[i], right[i]) - height[i]

            if diff > 0:
                ans += diff

        return ans