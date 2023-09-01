from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    tropeiro = Dish('tropeiro', 5.00)
    frango = Ingredient('frango')
    parmegiana = Dish('parmegiana', 50)
    parmegiana.add_ingredient_dependency(frango, 10)
    assert tropeiro.name == 'tropeiro'
    assert tropeiro.__eq__(Dish('tropeiro', 5.00))
    assert tropeiro.__repr__() == "Dish('tropeiro', R$5.00)"
    assert parmegiana.__hash__() != tropeiro.__hash__()
    assert parmegiana.__hash__() == Dish('parmegiana', 50).__hash__()
    assert frango in parmegiana.recipe
    assert frango in parmegiana.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in parmegiana.get_restrictions()
    print(parmegiana.get_restrictions())

    with pytest.raises(TypeError):
        wrg_price = Dish('lasanha', '50')
        wrg_price.price != 50
    with pytest.raises(ValueError):
        ngt_price = Dish('lasanha', -50)
        ngt_price.price != 50
