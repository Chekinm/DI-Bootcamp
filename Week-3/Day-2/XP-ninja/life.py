from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Cell():
    # hold coordinates of cell
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return(f'({self.x}, {self.y})')
        

class Map_state (dict):

    def __init__(self):
        super().__init__(self)
    
    def set_live(self, *cells:Cell) -> None:
        for cell in cells:
            if cell.x in self:
                self[cell.x][cell.y] = 1
            else:
                self[cell.x] = {cell.y:1}

    def set_dead(self, cell:Cell) -> None:
        self[cell.x].pop(cell.y) 
        if len(self[cell.x]) == 0:
            self.pop(cell.x)

    def get_surrounding(self) -> set:
        set_around = set()
        for x, dict_y in self.items():
            for y in dict_y.keys():
                for i in range(-1,2):
                    for j in range(-1,2):
                        set_around.add(Cell(x+i,y+j))
        return set_around
    
    def get_live(self):
        # need this function to print map using matplotlib
        x_arr=[]
        y_arr=[]
        for x, dict_y in self.items():
            for y in dict_y.keys():
               x_arr.append(x)
               y_arr.append(y) 
        return(x_arr, y_arr)

    def count_8(self, c):
        # calcualte number of neibor
        count = 0
        is_live = False
        for i in range(-1,2):
            for j in range(-1,2):
                if c.x + i in self and c.y + j in self[c.x + i]:
                    if i == 0 and j == 0:
                        is_live = True
                    else:
                        count += 1
        return count, is_live 
    
    def one_step(self):
        tmp_map = Map_state()
        set_around = self.get_surrounding()
        for cell in set_around:
            count, is_live = self.count_8(cell)
            if is_live:
                if  count == 2 or count == 3:
                    tmp_map.set_live(cell)
            else:
                if count == 3:
                    tmp_map.set_live(cell)
        
        
        return tmp_map

# initilize life

life = Map_state()

# seed random cell
from random import randint
for i in range(2000):
    c = Cell(randint(0,55),randint(0,63))
    life.set_live(c)


fig, ax = plt.subplots()
plt.axis('off')
    
# this function runs repeatedly due to a cycle in 
# anumation.FuncAnimation so we don't need anitional loop to 
# perform life recalculation

num_of_step = 100
# number of step between redraw of the map 

def update(frame):

    global life 
    # cannot find how to pass additional arguments to the func 
    # in the animation.FuncAutoamtion
    ax.clear()
    plt.axis('off')
    
    for i in range(num_of_step):
        life = life.one_step()
    to_draw = life.get_live()
    print(frame)

    scat = ax.scatter(to_draw[0], to_draw[1], c='b', marker = 's', linewidths= 1.0)
    
    return (scat)


def init():
    ax.clear()

ani = animation.FuncAnimation(fig=fig, func=update, frames=None, init_func=init)
plt.show()

 

