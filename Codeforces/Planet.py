test_cases = int(input())

def removeplanets():
    planets = {}
    min_cost = 0
    n, c = list(map(int, input().split()))
    
    planet_list = []
    planet_list = list(map(int, input().split()))
    
    for planet in planet_list:
        planets[planet] = 1 + planets.get(planet, 0)
    
    for key, val in planets.items():
        if val <= c:
            min_cost += val
        else:
            min_cost += c
            
    print(min_cost)
        
for _ in range(test_cases):
    removeplanets()
        
