class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        curr = ""
        ver1 = []
        ver2 = []
        for ch in version1 + ".":
            if ch == ".":
                ver1.append(curr)
                curr = ""
            else:
                curr += ch
        curr2 = ""
        for ch in version2 + ".":
            if ch == ".":
                ver2.append(curr2)
                curr2 = ""
            else:
                curr2 += ch
        i = 0
        j = 0
        while i < len(ver1) and j < len(ver2):
            if int(ver1[i]) > int(ver2[j]):
                return 1
            elif int(ver1[i]) < int(ver2[j]):
                return -1
            elif int(ver1[i]) == int(ver2[j]):
                i += 1
                j += 1
                continue
            i += 1
            j += 1
        while i < len(ver1):
            if int(ver1[i]) > 0:
                return 1
            elif int(ver1[i]) < 0:
                return -1
            elif int(ver1[i]) == 0:
                i += 1
                
                continue
        while j < len(ver2):
            if int(ver2[j]) > 0:
                return -1
            elif int(ver2[j]) < 0:
                return 1
            elif int(ver2[j]) == 0:
                j += 1
                
                continue
        return 0
                
            