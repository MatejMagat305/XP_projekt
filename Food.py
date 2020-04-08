from TestExceptions import *

class Food:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def __repr__(self):
        return f'{self.name}: {self.cost} euro'


class FoodDatabase:

    def __init__(self, file=None):
        self.all_food = list()

        if file is None:
            file = 'List_of_meals.txt'

        try:
            with open(file) as input_file:
                for riadok in input_file:
                    if ',' in riadok:
                        food_name, food_cost = riadok.split(',')
                        food = Food(food_name.lower().capitalize(), food_cost)
                        self.all_food.append(food)
        except FileNotFoundError:
            raise FileNotFoundError('File not found')

    def add_food(self, food):
        self.all_food.append(food)

    def remove_food(self, removing_food):
        for i, food in enumerate(self.all_food):
            if food.name == removing_food.name and food.cost == removing_food.cost:
                self.all_food.pop(i)
                return True
        return False

bol = False
try:
    database = FoodDatabase('List_of_meals.tx')
except FileNotFoundError:
    bol = True
TEST(bol, True, 'test konstruktora')

database = FoodDatabase()
TEST(len(database.all_food), 12, 'test konstruktora2')

food = Food('rezen', 5)
database = FoodDatabase()
database.add_food(food)
TEST(len(database.all_food), 13, 'test pridania jedla')

food = Food('rezen', 5)
database = FoodDatabase()
database.add_food(food)
database.remove_food(food)
TEST(len(database.all_food), 12, 'test odobratia jedla')
