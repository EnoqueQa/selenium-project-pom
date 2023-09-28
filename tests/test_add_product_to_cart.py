import time
from selenium import webdriver
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com")

#login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#Adding backpack to cart and checking if it has been added
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
time.sleep(3)

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Enoque")
driver.find_element(By.ID, "last-name").send_keys("Fernandes")
driver.find_element(By.ID, "postal-code").send_keys("58295-000")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()
time.sleep(3)

driver.find_element(By.ID, "back-to-products").click()

#Adding T-Shirt to cart and checking if it has been added
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']").is_displayed()
time.sleep(3)

#Return to display products
driver.find_element(By.ID, "continue-shopping").click()

#Adding Onesie to cart and checking if it has been added
driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Onesie']").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Onesie']").is_displayed()
time.sleep(3)

#Clicking no checkout button
driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Enoque")
driver.find_element(By.ID, "last-name").send_keys("Fernandes")
driver.find_element(By.ID, "postal-code").send_keys("58295-000")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
assert driver.find_element(By.XPATH, "//*[@class='complete-header']").is_displayed()
time.sleep(4)