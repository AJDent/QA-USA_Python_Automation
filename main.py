import data
from helpers import is_url_reachable

print(data.hello())  # Confirming data.py is working


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Add in S8
        URBAN_ROUTES_URL = data.URBAN_ROUTES_URL

        if is_url_reachable(URBAN_ROUTES_URL):
           print("Connected to the Urban Routes server")
        else:
           print("Cannot connect to Urban Routes server")
           pass

    def test_set_route(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8 # I commited again because i recall having this saved
        for i in range(2):
         print("Function created for order 2 ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass


# ✅ Ensure this code is OUTSIDE the class (after its definition)
if __name__ == "__main__":
    test = TestUrbanRoutes()  # Create an instance of the class
    test.test_set_route()
    test.test_select_plan()
    test.test_fill_phone_number()
    test.test_fill_card()
    test.test_comment_for_driver()
    test.test_order_blanket_and_handkerchiefs()
    test.test_order_2_ice_creams()
    test.test_car_search_model_appears()
