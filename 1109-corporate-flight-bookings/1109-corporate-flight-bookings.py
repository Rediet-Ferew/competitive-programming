class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # seats = [0] * (n + 1)
        # for i in range(len(bookings)):
        #     start, end, seat = bookings[i]
        #     for j in range(start, end + 1):
        #         seats[j] += seat
        # return seats[1:]
        seats = [0] * n
        for book in bookings:
            start, end, seat = book
            if start > 1:
                seats[start - 2] += -seat
            seats[end - 1] += seat
        for i in range(n-2, -1, -1):
            seats[i] += seats[i+1]
        return seats