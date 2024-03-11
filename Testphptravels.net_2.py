# Selenium Python Task:
# 1. Go to URL: https://www.phptravels.net/
# 2. Login with email and pasword
# 3. Verify Login is successful
# 4. Go to flights page
# 5. Select a radio button (one way / multiway)
# 6. Select a flying from option
# 7. Select a destination to option
# 8. Select a departed date
# 9. Select travelers (Adult 2, Clild 1, Infant 1)
# 10. Select a flight type/ class
# 11. Search a flight
# 12. Verify that the flight search is successful


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

browser = "chrome"  # chrome, firefox, edge
driver = ''
flightType = "oneway"  # oneway, return

if browser == "chrome":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
else:
    driver = webdriver.Chrome()

driver.get('https://www.phptravels.net/')
driver.maximize_window()

# Login
time.sleep(15)
driver.find_element('xpath', "//strong[@class='m-0 text-dark']").click()
time.sleep(3)
driver.find_element('xpath', "//a[normalize-space()='Login']").click()
time.sleep(15)
driver.find_element('xpath', "//input[@id='email']").send_keys('user@phptravels.com')
driver.find_element('xpath', "//input[@id='password']").send_keys('demouser')
time.sleep(3)
driver.find_element('xpath', "//button[@id='submitBTN']").click()

time.sleep(5)
actual_title = driver.title
expected_title = "Dashboard"
if actual_title == expected_title:
    print('Login test Successful')
else:
    print('Login test Failed')

time.sleep(10)
driver.find_element('xpath', "(//a[normalize-space()='Flights'])[1]").click()


# Scrolling down the window
time.sleep(5)
driver.execute_script("window.scrollTo(0, window.scrollY + 100)")

# Selecting the flight type - One Way or Round Trip
radio_list = driver.find_elements(By.NAME, "trip")

for rbtn in radio_list:
    rbtn_attr = rbtn.get_attribute("value")
    print(rbtn_attr)
    if rbtn_attr == flightType:
        if rbtn.is_selected():
            print("The radio button is already selected")
        else:
            rbtn.click()
            print("The radio button is selected")
        break

# Select flying from Dhaka,Bangladesh
time.sleep(5)
#  driver.find_element('xpath', "//input[@id='one-way']").click()
driver.find_element('xpath', "(//div[@class='mt-2'])[1]").click()
time.sleep(3)
driver.find_element('xpath', "//input[@role='searchbox']").send_keys("DAC")
time.sleep(3)
driver.find_element('xpath', "//div[@class='mx-2']").click()

# Select destination to JFK,NY
time.sleep(5)
driver.find_element('xpath', "(//div[@class='mt-2'])[2]").click()
time.sleep(3)
driver.find_element('xpath', "//input[@role='searchbox']").send_keys("JFK")
time.sleep(3)
driver.find_element('xpath', "//div[@class='mx-2']").click()

# Select Depart date 20-04-2024
time.sleep(5)
driver.find_element('xpath', "//input[@id='departure']").click()
time.sleep(5)
driver.find_element('xpath', "(//td[contains(text(),'20')])[1]").click()

# Select travelers number
time.sleep(5)
driver.find_element('xpath', "//a[@class='dropdown-toggle dropdown-btn travellers waves-effect']").click()
time.sleep(3)
driver.find_element('xpath', "(//*[name()='svg'])[13]").click()
time.sleep(3)
driver.find_element('xpath', "(//*[name()='svg'])[15]").click()
time.sleep(3)
driver.find_element('xpath', "(//*[name()='svg'])[17]").click()

# Select flight type Business
time.sleep(5)
driver.find_element('xpath', "//select[@id='flight_type']").click()
time.sleep(3)
driver.find_element('xpath', "//option[@value='business']").click()


# Click search button
time.sleep(5)
driver.find_element('xpath', "//button[@id='flights-search']//*[name()='svg']").click()
time.sleep(10)
actual_title = driver.title
expected_title = "Flights Result"
if actual_title == expected_title:
    print('Flights search test Successful')
else:
    print('Flights search test Failed')


driver.close()
