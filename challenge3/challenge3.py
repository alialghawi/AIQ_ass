
def read_roads_and_create_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            road = line.strip()
            town_a, town_b = road.split()
            if town_a not in adjacency_list:
                adjacency_list[town_a] = []
            if town_b not in adjacency_list:
                adjacency_list[town_b] = []
            adjacency_list[town_a].append(town_b)
            adjacency_list[town_b].append(town_a) 
    return adjacency_list

def place_malls(adjacency_list):
    malls = set()
    for town, neighbors in adjacency_list.items():
        if not town in malls and all(neighbor not in malls for neighbor in neighbors):
            malls.add(town)
    return malls

file_path = 'AIQ - Management Trainee Assignment - Challenge_3.txt'

adjacency_list = read_roads_and_create_adjacency_list(file_path)

malls = place_malls(adjacency_list)

print("Malls should be placed in the following towns:", malls)
