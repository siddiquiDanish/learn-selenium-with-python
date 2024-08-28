from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.wikipedia.org/")

search_text = driver.find_element(By.NAME, value= "search")
search_text.send_keys("Incredible India")
search_text.send_keys(Keys.ENTER)

title_text = driver.find_element(By.CSS_SELECTOR, "#firstHeading > span")
print(title_text.text)

# btn = driver.find_element(By.CSS_SELECTOR, value= "form button" )
# btn.click()


# driver.close()
