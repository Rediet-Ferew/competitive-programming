class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        for w, l in matches:
            if w not in players:
                players[w] = [1, 0]
            else:
                players[w][0] += 1
            if l not in players:
                players[l] = [0, 1]
            else:
                players[l][1]  += 1
        # print(players)
        answer_1 = []
        answer_2 = []
        for player in players.keys():
            if players[player][1] == 0:
                answer_1.append(player)
                continue
            if players[player][1] == 1:
                answer_2.append(player)
                continue
        answer_1.sort()
        answer_2.sort()
        answer = [answer_1, answer_2]
        return answer
        # for key, val in players.items():
        #     if val[1] == 0:
        #         answer[0].append(key)
        #     elif val[1] == 1:
        #         answer[1].append(key)
        # print(answer)