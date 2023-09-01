from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    frango = Ingredient('frango')
    frango_2 = Ingredient('frango')
    carne = Ingredient('carne')
    tropeiro = Ingredient('tropeiro')
    assert frango.__hash__() == frango_2.__hash__()
    assert frango.__repr__() == "Ingredient('frango')"
    assert frango.__eq__(frango_2)
    assert carne.__hash__() != frango_2.__hash__()
    assert len(tropeiro.restrictions) == 0
    assert tropeiro.name == 'tropeiro'
