class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.relations = defaultdict(list)
        self.relations[kingName] = []
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:

        self.relations[parentName].append(childName)

    def death(self, name: str) -> None:

        self.dead.add(name)

    def successor(self, node, curr_order):

            if node not in self.dead:
                curr_order.append(node)

            for child in self.relations[node]:
                self.successor(child, curr_order)

    def getInheritanceOrder(self) -> List[str]:

        curr_order = []
        
        self.successor(self.kingName, curr_order)
        return curr_order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()