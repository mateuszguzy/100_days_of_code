import bs4
import time
import requests
from selenium import webdriver
from selenium.common import exceptions
from webdriver_manager.firefox import GeckoDriverManager

# apartment requirements
LOCATION = "katowice"
ROOMS = "two"
PRICE_MIN = 100
PRICE_MAX = 1000
AREA_MIN = 25
AREA_MAX = 50
# URLS
GOOGLE_FORMS = \
    "https://forms.gle/LMU3VB5KdVQYqTAF7"
FLAT_RENTING_PAGE = f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/{LOCATION}" \
                    f"?search[filter_float_price%3Afrom]={PRICE_MIN}" \
                    f"&search[filter_float_price%3Ato]={PRICE_MAX}" \
                    f"&search[filter_enum_rooms][0]={ROOMS}" \
                    f"&search[filter_float_m%3Afrom]={AREA_MIN}" \
                    f"&search[filter_float_m%3Ato]={AREA_MAX}"
flats = dict()

def fill_the_form():
    global flats
    print("Filling the form...")
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url=GOOGLE_FORMS)
    # fill the form based on "flats" dictionary
    # sometimes exception with non interactive element occurs, don't know why
    # that's why try method and program repeat
    try:
        for flat in flats:
            driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")\
                .send_keys(flats[flat]["location"])
            # send second data - price
            driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input") \
                .send_keys(flats[flat]["price"])
            # send third data - link to offer
            driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input") \
                .send_keys(flats[flat]["link"])
            # send form
            driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div").click()
            # fill another form
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    except exceptions.ElementNotInteractableException:
        time.sleep(5.0)
        main()
    finally:
        driver.quit()


def rental_page_scraping():
    global flats
    print("Web scraping...")
    # get page response and make soup out of it
    page_response = requests.get(url=FLAT_RENTING_PAGE)
    soup = bs4.BeautifulSoup(page_response.text, "html.parser")
    # search for all flats with omitting promoted ones
    all_flats = soup.find_all(name="table", id="offers_table", class_="fixed offers breakword redesigned")
    # lists to store data, will be used to make one dictionary out of all data
    links_list = list()
    locations_list = list()
    prices_list = list()
    # print(all_flats)
    # locate elements in the soup
    for flat in all_flats:
        # extract locations, prices and links
        locations_cell = flat.find_all(name="td", class_="bottom-cell")
        prices = flat.find_all(name="p", class_="price")
        # separate pictures with link from anchor text
        only_text = flat.find_all(name="td", class_="title-cell")
        # location need one extra extraction because of very similar elements that is a commercial
        for location_cell in locations_cell:
            locations = location_cell.find_all(name="p", class_="lheight16")
            for location in locations:
                locations_list.append(location.text.strip().split("\n\n\n"))
                # print(location.text.strip().split("\n\n\n"))
        for price in prices:
            prices_list.append(price.text.strip())
            # print(price.text.strip())
        # links need one additional sip from the soup after separation photos/text, right now anchor text href element
        # must be extracted
        for link in only_text:
            links = link.find_all(name="a")
            for single_link in links:
                links_list.append(single_link.get("href"))
                # print(single_link.get("href"))
    # make a dictionary out of extracted data
    for i in range(len(links_list)):
        try:
            flats[f"Flat_{i}"] = {
                "location": locations_list[i][0],
                "price": prices_list[i],
                "link": links_list[i],
            }
        except IndexError:
            pass


def main():
    rental_page_scraping()
    fill_the_form()


if __name__ == "__main__":
    main()
