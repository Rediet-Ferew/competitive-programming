class Solution:
    def numberToWords(self, num: int) -> str:
        limit = 1000000000000
        t = 0
        word = ""
        multiplier = ["", "Trillion", "Billion", "Million", "Thousand"]
        first_twenty = ["", "One", "Two",
                    "Three", "Four", "Five",
                    "Six", "Seven", "Eight",
                    "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen",
                    "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]
        tens = ["", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]
        if num < 20:
            return first_twenty[num]
        i = num
        while i > 0:
            curr_val = i // limit
            if curr_val > 99:
                word += (first_twenty[curr_val // 100] + " Hundred ")
            curr_val = curr_val % 100
            if (curr_val > 0 and curr_val < 20):
                word += (first_twenty[curr_val] + " ")
            elif (curr_val % 10 == 0 and curr_val != 0):
                word += (tens[(curr_val//10) - 1] + " ")
            elif (curr_val > 19 and curr_val < 100):
                word += (tens[(curr_val//10) - 1] + " " +
                       first_twenty[curr_val % 10] + " ")
            if (t < 4):
                word += (multiplier[t] + " ")
            i = i % limit
            limit = limit // 1000
        return word.strip()
            