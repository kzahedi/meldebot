from selenium import webdriver, common
from tqdm import tqdm
import datetime
import re


class Twitter(object):
    """
        Class to interact with twitter
    """

    def __init__(self):
        """ constructor """

        self.driver = None
        # click order: order in which buttons must be clicked for a reporting
        self.click_order = {}

        # Hass
        self.click_order["PR"] = ["germany-illegal-btn", "de-hate-speech-btn",
                                  "de-section-86-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["HK"] = ["germany-illegal-btn", "de-hate-speech-btn",
                                  "de-section-86a-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["VV"] = ["germany-illegal-btn", "de-hate-speech-btn",
                                  "de-section-130-btn", "de-someone-else-btn", "de-myself-btn"]

        # Terrorismus
        self.click_order["TV"] = ["germany-illegal-btn", "de-terrorism-btn",
                                  "de-section-129a-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["TVA"] = ["germany-illegal-btn", "de-terrorism-btn",
                                   "de-section-129b-btn", "de-someone-else-btn", "de-myself-btn"]

        # Gewalt - de-violence-btn:
        self.click_order["SG"] = ["germany-illegal-btn", "de-violence-btn",
                                  "de-section-89a-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["ASG"] = ["germany-illegal-btn", "de-violence-btn",
                                   "de-section-91-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["ÖAS"] = ["germany-illegal-btn", "de-violence-btn",
                                   "de-section-111-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["AN"] = ["germany-illegal-btn", "de-violence-btn",
                                  "de-section-126-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["KV"] = ["germany-illegal-btn", "de-violence-btn",
                                  "de-section-129-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["GD"] = ["germany-illegal-btn", "de-violence-btn",
                                  "de-section-131-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["BBS"] = ["germany-illegal-btn", "de-violence-btn",
                                   "de-section-140-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["BD"] = ["germany-illegal-btn", "de-violence-btn",
                                  "de-section-241-btn", "de-someone-else-btn", "de-myself-btn"]
        # Kindesmissbrauch:
        self.click_order["KM"] = ["germany-illegal-btn", "de-child-exploit-btn",
                                  "de-section-184b-btn", "de-someone-else-btn", "de-myself-btn"]

        # Beleidigung
        self.click_order["BR"] = ["germany-illegal-btn", "de-defamation-btn",
                                  "de-section-166-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["BE"] = ["germany-illegal-btn", "de-defamation-btn",
                                  "de-section-185-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["ÜN"] = ["germany-illegal-btn", "de-defamation-btn",
                                  "de-section-186-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["VE"] = ["germany-illegal-btn", "de-defamation-btn",
                                  "de-section-187-btn", "de-someone-else-btn", "de-myself-btn"]

        # Privacy
        self.click_order["PL"] = ["germany-illegal-btn", "de-privacy-btn",
                                  "de-section-201a-btn", "de-someone-else-btn", "de-myself-btn"]

        # Fälschung
        self.click_order["FB"] = ["germany-illegal-btn", "de-forgery-btn",
                                  "de-section-269-btn", "de-someone-else-btn", "de-myself-btn"]
        self.click_order["LVF"] = ["germany-illegal-btn", "de-forgery-btn",
                                   "de-section-100a-btn", "de-someone-else-btn", "de-myself-btn"]

        self.keys = ["PR", "HK", "VV", "TV", "TVA", "SG", "ASG", "ÖAS", "AN",
                     "KV", "GD", "BBS", "BE", "KM", "BR", "BE", "ÜN", "VE", "PL", "FB", "LVF"]
        self.re_keys = [re.compile(r'\b%s\b' % word) for word in self.keys]

    def login(self, filename=None):
        """ login to twitter """

        with open(filename, "w") as fd:
            lines = fd.readlines()

        self.driver = webdriver.Chrome()

        # set the window size that you need
        self.driver.set_window_size(1024, 768)
        self.selenium_running = True

        login = lines[0]
        password = lines[1]

        self.driver.get("https://twitter.com/login")
        login_field = self.driver.find_element_by_css_selector(
            "input.js-username-field.email-input.js-initial-focus")
        password_field = self.driver.find_element_by_css_selector(
            "input.js-password-field")

        login_field.clear()
        password_field.clear()

        login_field.send_keys(login)
        password_field.send_keys(password + "\n")
