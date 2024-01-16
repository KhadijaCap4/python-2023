
# Ce test utilise une fixture définit dans le fichier conftest.py
# Une fixture est un scénario de test réutilisable pour définir des préconditions constantes à des tests.
# Il est automatiquement importé et il suffit de l'ajouter dans les parenthèses du test.
# La variable "returned" par la fixture peut être utilisée directement.
def test_get_with_fixture(restaurant_reviews_with_two_restaurants):
    result = restaurant_reviews_with_two_restaurants.get_review("Cafe Mocha")
    assert result == {'review_text': "Great Coffe.", 'rating': 4}
    result2 = restaurant_reviews_with_two_restaurants.get_review("Cafe Burger")
    assert result2 == {'review_text': "Good Burger", 'rating': 3}

def test_add_menu_item(menu_instance):
    assert menu_instance.add_menu_item("Restaurant A", "Item 3", "Description 3", 8.99) == "Menu item added for Restaurant A."
    assert menu_instance.add_menu_item("Restaurant A", "Item 1", "Description 1", 10.99) == "Menu item already exists."
