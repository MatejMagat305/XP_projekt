from Food import Food, FoodDatabase
from TestExceptions import *

class Table:
    def __init__(self):
        self.free = False
        self.ordered_food = dict()

    def add_order(self, food, count=None):
        self.ordered_food[food] = count if count is not None and count > 0 else 1

    def storno(self, food, count=1):
        food_count = self.ordered_food[food]
        if food_count > count:
            self.ordered_food[food] -= count
        elif food_count == count:
            self.ordered_food.pop(food)
        else:
            raise Exception('Wrong count')

    def __len__(self):
        return len(self.ordered_food)

    def show_info(self):
        for prvok in self.ordered_food.items():
            print('Name of food: ' + prvok[0].getName() + '\nPrize: ' + str(prvok[0].getCost()) + ' euro \nCount: ' +  str(prvok[1]))
            print('----------------------------------------------------------------------------')

stol = Table()
TEST(len(stol), 0, 'prazny stol')

stol = Table()
food = Food('mnamka', 3.7)
stol.add_order(food)
TEST(len(stol), 1, 'jeden prvok')

stol = Table()
food = Food('mnamka', 3.7)
stol.add_order(food)
food = Food('fujky', 3.7)
stol.add_order(food)
stol.storno(food)
TEST(len(stol), 1, 'jeden z dvoch pridanych')

database = FoodDatabase()
stol = Table()
for prvok in database.all_food:
    stol.add_order(prvok)
stol.show_info()

TEST(len(stol), 12, 'pridanie objednavky pre stol')
