class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def IsIVP4(s):
            s = s.split(".")
            # print(s)
            if len(s) != 4:
                return False
            for num in s:
                if not num:
                    return False
                for ch in num:
                    if not ch.isdigit():
                        return False
                n = int(num)
                
                if len(str(n)) != len(num):
                    return False
                if n < 0 or n > 255:
                    return False
            return True
        def IsIVP6(s):
            s = s.split(":")
            # print(s)
            if len(s) != 8:
                return False
            for num in s:
                if len(num) < 1 or len(num) > 4:
                    return False
                for ch in num:
                    if ch.isdigit():
                        continue
                    else:
                        if ch not in "ABCDEFabcdef":
                            return False
            return True
        if IsIVP4(queryIP):
            return "IPv4"
        if IsIVP6(queryIP):
            return "IPv6"
        else:
            return "Neither"