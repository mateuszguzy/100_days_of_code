from selenium import webdriver
import threading
import time
import os

GECKO_DRIVER_PATH = os.environ.get("GECKO_DRIVER_PATH")
driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
URL = "https://orteil.dashnet.org/experiments/cookie/"
SHOP_ITEMS = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment",
              "buyMine", "buyFactory", "buyGrandma", "buyCursor"]


def shop_checker():
    for item in SHOP_ITEMS:
        # get amount of possessed cookies each time comparing to new item
        cookies_amount = int(driver.find_element_by_id("money").text)
        # get HTML element that can be "clicked"
        clickable_item = driver.find_element_by_id(f"{item}")
        # extract item name
        item_name = clickable_item.text.split("\n")[0].split("-")[0].strip()
        # extract split price that need to be joined
        price_list = clickable_item.text.split("\n")[0].split("-")[1].split(",")
        # final price
        item_price = int("".join(price_list))
        if item_price <= cookies_amount:
            clickable_item.click()
            print(f"{item_name} bought.")
    time.sleep(5.0)
    shop_checker()


def main():
    # open browser with clicker game
    driver.get(URL)
    # start function that checks every 5s if new item from shop is affordable
    threading.Timer(5.0, shop_checker).start()
    cookie = driver.find_element_by_id("cookie")
    # keep clicking cookie along with function that checks if new item to buy is available
    while True:
        cookie.click()


if __name__ == "__main__":
    main()
