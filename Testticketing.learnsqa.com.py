# Selenium Python Task-1:
# 1. Go to URL: https://ticketing.learnsqa.com/
# 2. Input Name, Email, Title, Content
# 3. Upload a attachment
# 4. Verify ticket submission is successful

# Selenium Python Task-2:
# 1. Go to URL: https://ticketing.learnsqa.com/
# 2. Go to login page
# 3. Input Email and Password
# 4. Check the rememberm me checkbox
# 5. Click on login
# 6. Verify login is successful
# 7. Click on user management manu
# 8. Go to permission page
# 9. Click on Show entries and select 50
# 10. Search any ID from searchbox
# 11. View the ID details by click on View button
# 12. Click on back to list
# 13. Check Edit and Delete button by clicking of any of the ID's
# 14. Verify Action buttons work succesfuly.
# 15. Go to Ticlets page
# 16. View any of the ID
# 17. Scrolling down
# 18. Leave a comment on commentbox
# 19. Verify comment submission successful
# 20. Click on Back to list button
# 21. Click on Logout
# 22. Verify successfully logout.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
import time

browser = "chrome"  # chrome, firefox, edge
driver = ''

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

driver.get("https://ticketing.learnsqa.com/login")
driver.maximize_window()

time.sleep(3)
driver.find_element("id","email").send_keys("admin@admin.com")
time.sleep(3)
driver.find_element("id","password").send_keys("password")
time.sleep(3)
driver.find_element("xpath","//input[@id='remember']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".btn").click()

act_title=driver.title
exp_title="Support Ticketing"

if act_title==exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')

#driver.get_screenshot_as_file("Login.png")

time.sleep(5)
driver.find_element("xpath", "//a[normalize-space()='User management']").click()
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='Permissions']").click()
time.sleep(3)
driver.find_element("xpath", "//select[@name='DataTables_Table_0_length']").click()
time.sleep(3)
driver.find_element("xpath", "(//option[@value='25'])[1]").click()
time.sleep(2)
driver.find_element("xpath", "//input[@type='search']").send_keys("11")
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='View']").click()
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='Back to list']").click()
time.sleep(2)
driver.find_element("xpath", "//input[@type='search']").send_keys("12")
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='Edit']").click()
time.sleep(3)
driver.find_element("xpath", "//input[@value='Save']").click()

actual_title=driver.title
expected_title="Support Ticketing"

if actual_title==expected_title:
    print('Action Buttons Test Successfully')
else:
    print('Action Buttons Test Failed')

driver.close()
