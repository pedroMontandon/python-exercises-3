# from multiset import Multiset
from src.models.dish import Dish
from src.models.dish import Ingredient
from csv import DictReader


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.menu = {}
        with open(source_path, 'r') as file:
            for line in DictReader(file):
                price = float(line['price'])
                amount = int(line['recipe_amount'])

                if line['dish'] not in self.menu:
                    self.menu[line['dish']] = Dish(line['dish'], price)
                self.menu[line['dish']].add_ingredient_dependency(
                    Ingredient(line['ingredient']), amount
                )
                self.dishes.add(self.menu[line['dish']])
