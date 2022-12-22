class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        matches.sort()
        for i in range(len(matches)):
            w, l = matches[i]
            if w not in players:
                players[w] = 0
            players[l] = 1+ players.get(l, 0)
        ans1, ans2 = [], []
        for k, v in players.items():
            if v == 0:
                ans1.append(k)
            if v == 1:
                ans2.append(k)
        return [ans1, sorted(ans2)]
            
        
        