class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 2)
        # for k in range(1, n + 1):
        #     prefix[k] = 0
        for book in bookings:
            first, last, seat = book
            prefix[first] += seat
            prefix[last + 1] -= seat
        temp = 0
        result = []
        for i in range(n + 1):
            temp += prefix[i]
            result.append(temp)
        return (result[1:])
            