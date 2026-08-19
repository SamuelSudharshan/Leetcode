class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:

        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        ans = 2 * n

        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            left_free = left.isdisjoint(seats)
            middle_free = middle.isdisjoint(seats)
            right_free = right.isdisjoint(seats)

            # Initially this row was counted as 2
            if left_free and right_free:
                continue

            # It can still fit one group
            if left_free or middle_free or right_free:
                ans -= 1
            else:
                # No possible group
                ans -= 2

        return ans