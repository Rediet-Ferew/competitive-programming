class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        mades = []
        adj_list = defaultdict(list)
        cnt = defaultdict(int)
        for j in range(len(recipes)):
            cnt[recipes[j]] = len(ingredients[j])
        for i in range(len(ingredients)):
            ing = ingredients[i]
            for ingr in ing:
                adj_list[ingr].append(recipes[i])
        q = collections.deque(supplies)
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                recipe = q.popleft()
                for r in adj_list[recipe]:
                    cnt[r] -= 1
                    if cnt[r] == 0:
                        mades.append(r)
                        q.append(r)
                        cnt.pop(r)
        
        return mades