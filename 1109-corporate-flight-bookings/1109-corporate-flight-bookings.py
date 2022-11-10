class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n+1)
        for book in bookings:
            start, end, seat = book
            seats[start] += seat
            if end < n:
                seats[end + 1] += -seat
        for i in range(1, n+1):
            seats[i] += seats[i-1]
        return seats[1:]