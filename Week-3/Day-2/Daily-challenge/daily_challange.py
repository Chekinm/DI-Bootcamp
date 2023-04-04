from string import ascii_lowercase
from math import ceil
# The Pagination class will accept 2 parameters:

class Pagination():

    def __init__(self, items=None, page_size=10) -> None:
        if items == None:
            self.items = []
        else:
            self.items = items 
        self.page_size = int(page_size)
        self.current_page = 0
        # I did it 0 based, as it is more natural for progrmming
        # we can + 1 or -1 it if we need to show it or get ir from input 
        self.num_of_page = ceil(len(items)/page_size)

    def getVisibleItems(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
    def prev_page(self):
        if self.current_page:
            slef.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.num_of_page:
            self.current_page += 1
        return self

    def firstPage(self):
        self.current_page = 0
        return self

    def lastPage(self):
        self.current_page = self.num_of_page - 1
        return self

    def go_to_page(self, page_num):
        if   0 <= page_num <= self.num_of_page:
            self.current_page = page_num
        elif page_num <=0:
            print('You are trying to access a page which doesn\'t exists')
            print('getting you closest page number')
            self.current_page = 0
        else:
            print('You are trying to access a page which doesn\'t exists')
            print('getting you closest page number')
            self.current_page = self.num_of_page - 1
        return self
        

p = Pagination(list(ascii_lowercase), 4)
p.go_to_page(4)
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.firstPage()
print(p.getVisibleItems())
p.next_page().next_page()
print(p.current_page, p.getVisibleItems())
print(p.num_of_page)