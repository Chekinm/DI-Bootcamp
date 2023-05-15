m = [
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,0],
    [1,0,1,0,0,0,1,0,0],
    [1,0,1,0,1,1,1,0,0],
    [1,0,1,0,1,0,1,0,0],
    [1,0,1,0,1,0,1,0,0],
    [1,0,0,0,1,0,0,0,0],
    [1,0,0,0,1,0,1,1,0],
    [1,1,1,1,1,0,0,0,1],
    ]

M = len(m)
list_of_islands = []  # list of sets, set 

class Cell(int):
    def __init__(self, value, is_boarder=False, island_number=None):
        super().__init__()
        self.value = value
        self.is_boarder = is_boarder
        self.island_number = island_number



def proced_cell(i, j, value, map, last_island_number):
    M = len(map)
    map[i][j].value = value
    if i == 0 or i == (M-1) or j == 0 or j == (M-1):
        map[i][j].is_boarder = True
    if value == 1:
        if map[i][j].island_number == None:
            last_island_number += 1
            map[i][j].island_number = last_island_number
        for k, p in [(i,j - 1),(i,j+1),(i-1,j),(i+1,j)]:
            if 0 <= k < M and  0 <= p < M:
                map[k][p].island_number = map[i][j].island_number
                if map[i][j].is_boarder:
                    map[k][p].is_boarder = map[i][j].is_boarder

    return map, last_island_number 

map = [[Cell(value) for value in row] for row in m]

last_island_number = 0
print(*map, sep='\n',end='\n\n')

for i in range(len(m)):
    for j in range(len(m[0])):
        map, last_island_number = proced_cell(i,j,m[i][j],map,last_island_number) 
print(*map, sep='\n',end='\n\n')


for i in range(len(m)):
    for j in range(len(m[0])):     
        if map[i][j].value == 1 and map[i][j].is_boarder == False:
            map[i][j] = Cell(0)

print(*map, sep='\n', end='\n\n')

   
for i in range(len(m)):
    for j in range(len(m[0])):  
        print(i,j,
              map[i][j].value,
              map[i][j].is_boarder,
              map[i][j].island_number)
