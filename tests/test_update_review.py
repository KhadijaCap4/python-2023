import pytest 
from restaurant_reviews import RestaurantReviews

def test_update_existing_review():
      rr = RestaurantReviews()
      rr.add_review("Sushi Spot", "Fresh and tasty sushi.", 4)
      update_result = rr.update_review("Sushi Spot", "Exceptional sushi and service.", 5) 
      get_result = rr.get_review("Sushi Spot")
      assert update_result == "Review added for Sushi Spot."
      assert get_result == {'review_text' : "Exceptional sushi and service.", 'rating' : 5}

def test_update_non_existing_review():
      rr = RestaurantReviews()
      result = rr.update_review("Grill House", "Best steaks in town.", 5)
      assert result == "Review not found."