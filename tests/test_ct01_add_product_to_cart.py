import time
import pytest
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage 


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.add_products
class TestCT01:
    def testct01_add_product_to_cart(self):
        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        checkout_step_one_page = CheckoutStepOnePage()
        checkout_step_two_page = CheckoutStepTwoPage()
        checkout_complete_page = CheckoutCompletePage()
        
        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Onesie"
        first_name_checkout = "Enoque"
        last_nam_checkout = "Fernandes"
        postal_code_checkout = "58295-000"
        expected_message_finish_order = "Thank you for your order!"
        
        #login
        login_page.login("standard_user","secret_sauce")

        #Adding backpack to cart
        home_page.click_product(product_1)
        home_page.click_button_add_to_cart()
        
        #Checking that the backpack has been added
        home_page.access_the_cart()
        cart_page.verify_product_cart_existing(product_1)

        # #Return to display products
        cart_page.click_continue_shopping()

        #Adding Onesie to cart and checking if it has been added
        home_page.click_product(product_2)
        home_page.click_button_add_to_cart()
        
        #Access the cart
        home_page.access_the_cart()
        
        #Verifry existing products to cart
        cart_page.verify_product_cart_existing(product_1)
        cart_page.verify_product_cart_existing(product_2)

        #Clicking no checkout button
        cart_page.click_button_checkout()
        
        #Fill in information at checkout   
        checkout_step_one_page.checkout_step_one(first_name_checkout, last_nam_checkout, postal_code_checkout)
        checkout_step_one_page.click_button_continue_checkout()
        
        # Click finish checkout
        checkout_step_two_page.click_finish_checkout()
        
        # Verify checkout with success
        checkout_complete_page.verify_checkout_with_success()
        checkout_complete_page.verify_text_message_finish_order(expected_message_finish_order)
