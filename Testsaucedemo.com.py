# Selenium Python Task:
# 1. Go to URL: https://www.saucedemo.com/
# 2. Log in with standard_user
# 3. Verify login is successful
# 4. Add a product to the cart
# 5. Go to cart and checkout
# 6. Enter name & postal code
# 7. Finish the purchase
# 8. Verify that the purchase is successful
# 8. Go back to homepage
# 9. Log out
# 10. Verify user is logged out successfully


from selenium import webdriver

#Webdriver script for Edge
# from selenium.webdriver.edge.options import Options
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Edge(options=options)

#Webdriver script for Firefox
driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

#Verify login
driver.find_element('id', 'user-name').send_keys('standard_user')
driver.find_element('name', 'password').send_keys('secret_sauce')
driver.find_element('xpath', "//input[@class='submit-button btn_action']").click()

act_title=driver.title
exp_title="Swag Labs"

if act_title==exp_title:
    print('Login test Successful')
else:
    print('Login test Failed')

#Verify purchase using xpath
driver.find_element('xpath', "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element('xpath', "//a[@class='shopping_cart_link']").click()
driver.find_element('xpath', "//button[@id='checkout']").click()
driver.find_element('xpath', "//input[@id='first-name']").send_keys('Bob')
driver.find_element('xpath', "//input[@id='last-name']").send_keys('Dylan')
driver.find_element('xpath', "//input[@id='postal-code']").send_keys('3583')
driver.find_element('xpath', "//input[@id='continue']").click()
driver.find_element('xpath', "//button[@id='finish']").click()

act_title=driver.title
exp_title="Swag Labs"

if act_title==exp_title:
    print('Purchase test Successful')
else:
    print('Purchase test Failed')

#Verify logout using css selector
driver.find_element('css selector', "#back-to-products").click()
driver.find_element('css selector', "#react-burger-menu-btn").click()
driver.find_element('css selector', "#logout_sidebar_link").click()

act_title=driver.title
exp_title="Swag Labs"

if act_title==exp_title:
    print('Logout test Successful')
else:
    print('Logout test Failed')

driver.close()