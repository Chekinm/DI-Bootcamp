import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint


class Cell():
    # hold coordinates of cell
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Map_state (dict):

    def __init__(self):
        super().__init__(self)
        self.amount = 0

    def set_live(self, *cells: Cell) -> None:
        for cell in cells:
            if cell.x in self:
                self[cell.x][cell.y] = 1
            else:
                self[cell.x] = {cell.y: 1}
            self.amount += 1

    def set_dead(self, cell: Cell) -> None:
        self[cell.x].pop(cell.y)
        if len(self[cell.x]) == 0:
            self.pop(cell.x)
        self.amount -= 1

    def get_surrounding(self) -> set:
        set_around = set()
        for x, dict_y in self.items():
            for y in dict_y.keys():
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        set_around.add(Cell(x+i, y+j))
        return set_around

    def get_live(self):
        # need this function to print map using matplotlib
        x_arr = []
        y_arr = []
        for x, dict_y in self.items():
            for y in dict_y.keys():
                x_arr.append(x)
                y_arr.append(y)
        return (x_arr, y_arr)

    def count_8(self, c):
        # calculate number of neighbors
        count = 0
        is_live = False
        for i in range(-1, 2):
            for j in range(-1, 2):
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
                if count == 2 or count == 3:
                    tmp_map.set_live(cell)
            else:
                if count == 3:
                    tmp_map.set_live(cell)
        return tmp_map


# initilize life
life = Map_state()

# seed random cell
num_of_cell = int(input('Enter number of cell to randomly seed: '))
x_size = int(input('Enter x_size of the initial field to seed: '))
y_size = int(input('Enter y_size of the initial field to seed: '))

for i in range(num_of_cell):
    c = Cell(randint(0, x_size), randint(0, y_size))
    life.set_live(c)

fig, ax = plt.subplots()
plt.axis('equal')
plt.axis('off')

# this function runs repeatedly due to a cycle in
# anumation.FuncAnimation so we don't need anitional loop to
# perform life recalculation

redraw_steps = int(input('Enter number of step to skip to draw'
                         'new picture like every step or every'
                         '10 steps or every 500 steps): '))
# number of step between redraw of the map
steps = int(input('Enter number of draw iteration'
                  ', 0 means inifinite iteration: '))
if steps == 0:
    steps = None


def update(frame):

    global life
    # cannot find a good way to pass additional arguments to the func
    # in the FuncAnimation
    ax.clear()
    plt.axis('off')

    for i in range(redraw_steps):
        life = life.one_step()
    to_draw = life.get_live()
    print(frame, life.amount)

    scat = ax.scatter(to_draw[0], to_draw[1], c='b', linewidths=0.1)

    return (scat)


def init():
    ax.clear()
    plt.axis('off')


ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=steps,
                              repeat=False,
                              init_func=init)
plt.show()
