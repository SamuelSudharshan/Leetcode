import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:

        def can_finish(T):
            total = 0

            for t in workerTimes:
                val = (2 * T) // t
                k = int((math.sqrt(1 + 4 * val) - 1) // 2)
                total += k

                if total >= mountainHeight:
                    return True

            return False

        left = 0
        right = 10**18

        while left < right:
            mid = (left + right) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left