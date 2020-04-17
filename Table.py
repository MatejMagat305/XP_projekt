from Food import Food, FoodDatabase
from TestExceptions import *


class Table:
    def __init__(self, free=True):
        self.free = free
        self.ordered_food = dict()  # Food: [pocet_objednanych, pocet_kolko_uz_bolo_spravenych]

    def add_order(self, food, count=None):
        if food in self.ordered_food:
            self.ordered_food[food][0] += 1
            return
        self.ordered_food[food] = [count, 0] if count is not None and count > 0 else [1, 0]

    def add_done(self, food):
        if all(food.name != food_in.name for food_in in self.ordered_food):
            raise FoodNotExists('This food doesn\'t exist')
        if self.ordered_food[food][0] <= self.ordered_food[food][1]:
            raise WrongCountDone('You cannot make done order that is already done')

        self.ordered_food[food][1] += 1

    def storno(self, food, count=1):
        food_count = self.ordered_food[food][0]
        if food_count > count:
            self.ordered_food[food][0] -= count
        elif food_count == count:
            self.ordered_food.pop(food)
        else:
            raise StornoWrongCount('You want to storno more food than customers ordered.')

    def __len__(self):
        return len(self.ordered_food)

    def show_info(self):
        for ordered_food in self.ordered_food.items():
            food_name = ordered_food[0].getName()
            food_cost = str(ordered_food[0].getCost())
            food_count = str(ordered_food[1][0])
            print('Name of food: ' + food_name + '\nPrize: ' + food_cost + ' euro \nCount: ' + food_count)
            print('----------------------------------------------------------------------------')


stol = Table()
TEST(len(stol), 0, 'prazdny stol')

stol = Table(False)
food = Food('mnamka', 3.7)
stol.add_order(food)
TEST(len(stol), 1, 'jeden prvok')

stol = Table(False)
food = Food('mnamka', 3.7)
stol.add_order(food)
food = Food('fujky', 3.7)
stol.add_order(food)
stol.storno(food)
TEST(len(stol), 1, 'jeden z dvoch pridanych')

stol = Table(False)
food = Food('mnamka', 3.7)
stol.add_order(food)
food = Food('fujky', 4)
stol.add_order(food, 5)
try:
    stol.storno(food, 6)
    TEST(True, False, 'chyba poctu stornovania')
except StornoWrongCount:
    pass

database = FoodDatabase()
stol = Table(False)
for prvok in database.all_food:
    stol.add_order(prvok)
stol.show_info()

TEST(len(stol), 12, 'pridanie objednavky pre stol')

stol = Table(False)
food = Food('mnamka', 3.7)
stol.add_order(food)
food = Food('fujky', 3.7)
stol.add_order(food)
stol.add_done(food)
TEST(1, stol.ordered_food[food][1], 'pocet urobenych')

stol = Table(False)
food = Food('mnamka', 3.7)
stol.add_order(food)
food = Food('fujky', 3.7)
stol.add_order(food)
try:
    stol.add_done(Food('mnamka2', 3.7))
    TEST(True, False, 'neexistuje order')
except FoodNotExists:
    pass
