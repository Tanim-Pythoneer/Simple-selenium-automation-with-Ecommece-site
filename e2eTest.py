from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# First locate the chrome extension and get the site I want to experiment
driver = webdriver.Chrome(executable_path='/Users/tanimkamal/Downloads/chromedriver 2')
driver.get("https://rahulshettyacademy.com/angularpractice/")

#From here I will start to automate the dummy website..
#Goal is to by use shop button, we get blackberry product and proceed with checkout then print the success message...
driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()
#To add the specific Blackberry product, I selected the parent css and used for loop to find Blackberry and click it..
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

#After selecting Blackberry phone, now I will assert if Blackberry exists in 'ordered' page..
blackberry = driver.find_element_by_link_text("Blackberry").text
assert blackberry in productName

#After succesful order, I will click to checktout(1) and follow to next page..
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class*='success']").click()
driver.find_element_by_id("country").send_keys("bangla")

#I used explicit wait as after input it takes a while to load the designated address..
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Bangladesh')))
driver.find_element_by_link_text("Bangladesh").click()
driver.find_element_by_xpath("//label[contains(text(),'I agree with the ')]").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()
success_text = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you!" in success_text

#I will take a screenshot now, just to demonstrate how screenshot works..
driver.get_screenshot_as_file("screen.png")


