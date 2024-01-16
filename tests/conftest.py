import pytest
from restaurant_reviews import RestaurantReviews
from menu import Menu
# Fixture : Définition d'un scério réutilisable dans les tests
@pytest.fixture
def restaurant_reviews_with_two_restaurants():
    rr = RestaurantReviews()
    # Ajout des restaurants pour mes scénario
    rr.add_review("Cafe Mocha", "Great Coffe.", 4)
    rr.add_review("Cafe Burger", "Good Burger", 3)
    return rr

@pytest.fixture
def menu_instance():
    menu = Menu()
    menu.add_menu_item("Restaurant A", "Item 1", "Description 1", 10.99)
    menu.add_menu_item("Restaurant B", "Item 2", "Description 2", 15.99)
    return menu
