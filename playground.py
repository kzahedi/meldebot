# %%
from selenium import webdriver
import time

# %%
with open("log_ga.txt", "r") as fd:
    lines = fd.readlines()

login = lines[0]
password = lines[1]

# %%
driver = webdriver.Chrome()

# %%
# set the window size that you need
driver.set_window_size(1024, 768)
selenium_running = True

# %%
driver.get("https://twitter.com/login")
time.sleep(3)
# %%
login_field = driver.find_element_by_xpath("//input")

login_field.clear()
# password_field.clear()

login_field.send_keys(login)
# password_field.send_keys(password + "\n")

# %%
time.sleep(2)
password_field = driver.find_element_by_xpath("//input[@name='password']")
password_field.send_keys(password + "\n")

# %% boost your account screen

# try:
close = driver.find_element_by_xpath("//div[@aria-label=\"Close\"]")
close.click()
# except NoSuchElementException:
# print("Close button not found")
# pass

# %% boost your account screen

# try:
close = driver.find_element_by_xpath("//div[@aria-label=\"Close\"]")
close.click()
# except NoSuchElementException:
# print("Close button not found")
# pass


# %% Accept all cookies button

accept_all_cookies = driver.find_element_by_xpath(
    "//*[text()='Accept all cookies']")
accept_all_cookies.click()

# %% open tweet

driver.get("https://twitter.com/Hartes_Geld/status/1598421244982054912")

# %%
