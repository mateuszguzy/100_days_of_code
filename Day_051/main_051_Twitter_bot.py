import os
import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


PROMISED_UP = 1000
PROMISED_DOWN = 1000
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://mobile.twitter.com/i/flow/login"
TWITTER_USER = os.environ.get("TEST_TWITTER_USER")
TWITTER_PASSWORD = os.environ.get("TEST_TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        # using web driver manager, every time install latest version of driver
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.down = int()
        self.up = int()

    def get_internet_speed(self):
        # print("Checking internet speed.")
        # open speed test URL
        self.driver.get(url=SPEED_TEST_URL)
        # if cookie consent is visible, make it, if not pass
        try:
            accept_cookies = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
            accept_cookies.click()
        except exceptions.NoSuchElementException:
            pass
        # start test with GO butoon
        self.driver.find_element_by_class_name("start-text").click()
        # print("Waiting for test to finish...")
        # wait for test to end
        time.sleep(60.0)
        # assign download and upload values to Object attributes
        self.down = float(self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/"
                                                            "div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/"
                                                            "div[2]/span").text)

        self.up = float(self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/"
                                                          "div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/"
                                                          "span").text)
        # print(f"Download: {self.down}\nUpload: {self.up}")
        # if real internet speed is lower then signed, tweet a complaint
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            return True
        else:
            return False

    def post_a_tweet(self, message):
        # print("Logging into Twitter.")
        # open Twitter page
        self.driver.get(TWITTER_URL)
        # using expected conditions there is no need to use time.sleep function, because program will resume as soon as
        # searched elements will appear on a screen
        # wait for element to load and if found input username
        WebDriverWait(self.driver, 10)\
            .until(ec.visibility_of_element_located((By.TAG_NAME, "input")))\
            .send_keys(TWITTER_USER)
        # click "Next" to go to next page
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((
            By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                      "div[2]/div/div/div[2]/div[2]/div[2]/div/div"))).click()
        # wait for password input to load and insert user password
        WebDriverWait(self.driver, 10) \
            .until(ec.visibility_of_element_located((By.TAG_NAME, "input"))) \
            .send_keys(TWITTER_PASSWORD)
        # log in
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((
            By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/"
                      "div[2]/div/div/div[2]/div[2]/div[2]/div/div"))).click()
        # print("Posting a tweet.")
        # locate message input and place message there
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/"
                      "div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")))\
            .send_keys(f"{message}")
        # post a tweet
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
        #     By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/
        #     div/div[2]/div[3]/div/div/div[2]/div[3]"))).click()


def main():
    bot = InternetSpeedTwitterBot()
    internet_is_slow = bot.get_internet_speed()
    if internet_is_slow:
        message = "TEST MESSAGE!\n"\
                  "Hello Internet provider.\n" \
                  f"Why is my internet speed {bot.down}up/{bot.up}down, " \
                  f"while I pay for {PROMISED_DOWN}up/{PROMISED_UP}down?"
        bot.post_a_tweet(message)


if __name__ == "__main__":
    main()
