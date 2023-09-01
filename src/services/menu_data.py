# from multiset import Multiset
from src.models.dish import Dish
from src.models.dish import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.menu = {}
        with open(source_path, 'r') as file:
            for line in file:
                data = line.split(',')
                name = data[0]
                price = float(data[1])
                ingredient = data[2]
                amount = int(data[3])

                if name not in self.menu:
                    self.menu[name] = Dish(name, price)
                self.menu[name].add_ingredient_dependency(
                    Ingredient(ingredient), amount
                )
                self.dishes.add(self.menu[name])
